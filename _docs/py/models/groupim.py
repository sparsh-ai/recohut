# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/models/models.groupim.ipynb (unless otherwise specified).

__all__ = ['GroupIM']

# Cell
import torch
import torch.nn as nn
import torch.nn.functional as F

# Internal Cell
class Encoder(nn.Module):
    """ User Preference Encoder implemented as fully connected layers over binary bag-of-words vector
    (over item set) per user """

    def __init__(self, n_items, user_layers, embedding_dim, drop_ratio):
        super(Encoder, self).__init__()
        self.n_items = n_items
        self.embedding_dim = embedding_dim
        self.drop = nn.Dropout(drop_ratio)
        self.user_preference_encoder = torch.nn.ModuleList()  # user individual preference encoder layers.

        for idx, (in_size, out_size) in enumerate(zip([self.n_items] + user_layers[:-1], user_layers)):
            layer = torch.nn.Linear(in_size, out_size, bias=True)
            nn.init.xavier_uniform_(layer.weight)
            nn.init.zeros_(layer.bias)
            self.user_preference_encoder.append(layer)

        self.transform_layer = nn.Linear(self.embedding_dim, self.embedding_dim)
        nn.init.xavier_uniform_(self.transform_layer.weight)
        nn.init.zeros_(self.transform_layer.bias)

        self.user_predictor = nn.Linear(self.embedding_dim, self.n_items, bias=False)  # item embedding for pre-training
        nn.init.xavier_uniform_(self.user_predictor.weight)

    def pre_train_forward(self, user_items):
        """ user individual preference encoder (excluding final layer) for user-item pre-training
            :param user_items: [B, G, I] or [B, I]
        """
        user_items_norm = F.normalize(user_items)  # [B, G, I] or [B, I]
        user_pref_embedding = self.drop(user_items_norm)
        for idx, _ in enumerate(range(len(self.user_preference_encoder))):
            user_pref_embedding = self.user_preference_encoder[idx](user_pref_embedding)  # [B, G, D] or [B, D]
            user_pref_embedding = torch.tanh(user_pref_embedding)  # [B, G, D] or [B, D]

        logits = self.user_predictor(user_pref_embedding)  # [B, G, D] or [B, D]
        return logits, user_pref_embedding

    def forward(self, user_items):
        """ user individual preference encoder
            :param user_items: [B, G, I]
        """
        _, user_embeds = self.pre_train_forward(user_items)  # [B, G, D]
        user_embeds = torch.tanh(self.transform_layer(user_embeds))  # [B, G, D]
        return user_embeds

# Internal Cell
class MaxPoolAggregator(nn.Module):
    """ Group Preference Aggregator implemented as max pooling over group member embeddings """

    def __init__(self, input_dim, output_dim, drop_ratio=0):
        super(MaxPoolAggregator, self).__init__()

        self.mlp = nn.Sequential(
            nn.Linear(input_dim, output_dim, bias=True),
            nn.ReLU(),
            nn.Dropout(drop_ratio)
        )
        nn.init.xavier_uniform_(self.mlp[0].weight)
        if self.mlp[0].bias is not None:
            self.mlp[0].bias.data.fill_(0.0)

    def forward(self, x, mask, mlp=False):
        """ max pooling aggregator:
            :param x: [B, G, D]  group member embeddings
            :param mask: [B, G]  -inf/0 for absent/present
            :param mlp: flag to add a linear layer before max pooling
        """
        if mlp:
            h = torch.tanh(self.mlp(x))
        else:
            h = x

        if mask is None:
            return torch.max(h, dim=1)
        else:
            res = torch.max(h + mask.unsqueeze(2), dim=1)
            return res.values

# Internal Cell
# mask:  -inf/0 for absent/present.
class MeanPoolAggregator(nn.Module):
    """ Group Preference Aggregator implemented as mean pooling over group member embeddings """

    def __init__(self, input_dim, output_dim, drop_ratio=0):
        super(MeanPoolAggregator, self).__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_dim, output_dim, bias=True),
            nn.ReLU(),
            nn.Dropout(drop_ratio)
        )
        nn.init.xavier_uniform_(self.mlp[0].weight)
        if self.mlp[0].bias is not None:
            self.mlp[0].bias.data.fill_(0.0)

    def forward(self, x, mask, mlp=False):
        """ mean pooling aggregator:
            :param x: [B, G, D]  group member embeddings
            :param mask: [B, G]  -inf/0 for absent/present
            :param mlp: flag to add a linear layer before mean pooling
        """
        if mlp:
            h = torch.tanh(self.mlp(x))
        else:
            h = x
        if mask is None:
            return torch.mean(h, dim=1)
        else:
            mask = torch.exp(mask)
            res = torch.sum(h * mask.unsqueeze(2), dim=1) / mask.sum(1).unsqueeze(1)
            return res

# Internal Cell
class AttentionAggregator(nn.Module):
    """ Group Preference Aggregator implemented as attention over group member embeddings """

    def __init__(self, input_dim, output_dim, drop_ratio=0):
        super(AttentionAggregator, self).__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_dim, output_dim, bias=True),
            nn.ReLU(),
            nn.Dropout(drop_ratio)
        )

        self.attention = nn.Linear(output_dim, 1)
        self.drop = nn.Dropout(drop_ratio)
        nn.init.xavier_uniform_(self.mlp[0].weight)
        if self.mlp[0].bias is not None:
            self.mlp[0].bias.data.fill_(0.0)

    def forward(self, x, mask, mlp=False):
        """ attentive aggregator:
            :param x: [B, G, D]  group member embeddings
            :param mask: [B, G]  -inf/0 for absent/present
            :param mlp: flag to add a linear layer before attention
        """
        if mlp:
            h = torch.tanh(self.mlp(x))
        else:
            h = x

        attention_out = torch.tanh(self.attention(h))
        if mask is None:
            weight = torch.softmax(attention_out, dim=1)
        else:
            weight = torch.softmax(attention_out + mask.unsqueeze(2), dim=1)
        ret = torch.matmul(h.transpose(2, 1), weight).squeeze(2)
        return ret

# Internal Cell
class Discriminator(nn.Module):
    """ Discriminator for Mutual Information Estimation and Maximization, implemented with bilinear layers and
    binary cross-entropy loss training """

    def __init__(self, embedding_dim=64):
        super(Discriminator, self).__init__()
        self.embedding_dim = embedding_dim

        self.fc_layer = torch.nn.Linear(self.embedding_dim, self.embedding_dim, bias=True)
        nn.init.xavier_uniform_(self.fc_layer.weight)
        nn.init.zeros_(self.fc_layer.bias)

        self.bilinear_layer = nn.Bilinear(self.embedding_dim, self.embedding_dim, 1)  # output_dim = 1 => single score.
        nn.init.zeros_(self.bilinear_layer.weight)
        nn.init.zeros_(self.bilinear_layer.bias)

        self.bce_loss = nn.BCEWithLogitsLoss()

    def forward(self, group_inputs, user_inputs, group_mask):
        """ bilinear discriminator:
            :param group_inputs: [B, I]
            :param user_inputs: [B, n_samples, I] where n_samples is either G or # negs
            :param group_mask: [B, G]
        """
        # FC + activation.
        group_encoded = self.fc_layer(group_inputs)  # [B, D]
        group_embed = torch.tanh(group_encoded)  # [B, D]

        # FC + activation.
        user_pref_embedding = self.fc_layer(user_inputs)
        user_embed = torch.tanh(user_pref_embedding)  # [B, n_samples, D]

        return self.bilinear_layer(user_embed, group_embed.unsqueeze(1).repeat(1, user_inputs.shape[1], 1))

    def mi_loss(self, scores_group, group_mask, scores_corrupted, device='cpu'):
        """ binary cross-entropy loss over (group, user) pairs for discriminator training
            :param scores_group: [B, G]
            :param group_mask: [B, G]
            :param scores_corrupted: [B, N]
            :param device (cpu/gpu)
         """
        batch_size = scores_group.shape[0]
        pos_size, neg_size = scores_group.shape[1], scores_corrupted.shape[1]

        one_labels = torch.ones(batch_size, pos_size).to(device)  # [B, G]
        zero_labels = torch.zeros(batch_size, neg_size).to(device)  # [B, N]

        labels = torch.cat((one_labels, zero_labels), 1)  # [B, G+N]
        logits = torch.cat((scores_group, scores_corrupted), 1).squeeze(2)  # [B, G + N]

        mask = torch.cat((torch.exp(group_mask), torch.ones([batch_size, neg_size]).to(device)),
                         1)  # torch.exp(.) to binarize since original mask has -inf.

        mi_loss = self.bce_loss(logits * mask, labels * mask) * (batch_size * (pos_size + neg_size)) \
                  / (torch.exp(group_mask).sum() + batch_size * neg_size)

        return mi_loss

# Cell
class GroupIM(nn.Module):
    """
    GroupIM framework for Group Recommendation:
    (a) User Preference encoding: user_preference_encoder
    (b) Group Aggregator: preference_aggregator
    (c) InfoMax Discriminator: discriminator
    """

    def __init__(self, n_items, user_layers, lambda_mi=0.1, drop_ratio=0.4, aggregator_type='attention'):
        super(GroupIM, self).__init__()
        self.n_items = n_items
        self.lambda_mi = lambda_mi
        self.drop = nn.Dropout(drop_ratio)
        self.embedding_dim = user_layers[-1]
        self.aggregator_type = aggregator_type

        self.user_preference_encoder = Encoder(self.n_items, user_layers, self.embedding_dim, drop_ratio)

        if self.aggregator_type == 'maxpool':
            self.preference_aggregator = MaxPoolAggregator(self.embedding_dim, self.embedding_dim)
        elif self.aggregator_type == 'meanpool':
            self.preference_aggregator = MeanPoolAggregator(self.embedding_dim, self.embedding_dim)
        elif self.aggregator_type == 'attention':
            self.preference_aggregator = AttentionAggregator(self.embedding_dim, self.embedding_dim)
        else:
            raise NotImplementedError("Aggregator type {} not implemented ".format(self.aggregator_type))

        self.group_predictor = nn.Linear(self.embedding_dim, self.n_items, bias=False)
        nn.init.xavier_uniform_(self.group_predictor.weight)

        self.discriminator = Discriminator(embedding_dim=self.embedding_dim)

        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.xavier_uniform_(m.weight)
            if isinstance(m, nn.Embedding):
                nn.init.xavier_uniform_(m.weight)

    def forward(self, group, group_users, group_mask, user_items):
        """ compute group embeddings and item recommendations by user preference encoding, group aggregation and
        item prediction
        :param group: [B] group id
        :param group_users: [B, G] group user ids with padding
        :param group_mask: [B, G] -inf/0 for absent/present user
        :param user_items: [B, G, I] individual item interactions of group members
        """
        user_pref_embeds = self.user_preference_encoder(user_items)
        group_embed = self.preference_aggregator(user_pref_embeds, group_mask, mlp=False)  # [B, D]
        group_logits = self.group_predictor(group_embed)  # [B, I]

        if self.train:
            obs_user_embeds = self.user_preference_encoder(user_items)  # [B, G, D]
            scores_ug = self.discriminator(group_embed, obs_user_embeds, group_mask).detach()  # [B, G]
            return group_logits, group_embed, scores_ug
        else:
            return group_logits, group_embed

    def multinomial_loss(self, logits, items):
        """ multinomial likelihood with softmax over item set """
        return -torch.mean(torch.sum(F.log_softmax(logits, 1) * items, -1))

    def user_loss(self, user_logits, user_items):
        return self.multinomial_loss(user_logits, user_items)

    def infomax_group_loss(self, group_logits, group_embeds, scores_ug, group_mask, group_items, user_items,
                           corrupted_user_items, device='cpu'):
        """ loss function with three terms: L_G, L_UG, L_MI
            :param group_logits: [B, G, I] group item predictions
            :param group_embeds: [B, D] group embedding
            :param scores_ug: [B, G] discriminator scores for group members
            :param group_mask: [B, G] -inf/0 for absent/present user
            :param group_items: [B, I] item interactions of group
            :param user_items: [B, G, I] individual item interactions of group members
            :param corrupted_user_items: [B, N, I] individual item interactions of negative user samples
            :param device: cpu/gpu
        """

        group_user_embeds = self.user_preference_encoder(user_items)  # [B, G, D]
        corrupt_user_embeds = self.user_preference_encoder(corrupted_user_items)  # [B, N, D]

        scores_observed = self.discriminator(group_embeds, group_user_embeds, group_mask)  # [B, G]
        scores_corrupted = self.discriminator(group_embeds, corrupt_user_embeds, group_mask)  # [B, N]

        mi_loss = self.discriminator.mi_loss(scores_observed, group_mask, scores_corrupted, device=device)

        ui_sum = user_items.sum(2, keepdim=True)  # [B, G]
        user_items_norm = user_items / torch.max(torch.ones_like(ui_sum), ui_sum)  # [B, G, I]
        gi_sum = group_items.sum(1, keepdim=True)
        group_items_norm = group_items / torch.max(torch.ones_like(gi_sum), gi_sum)  # [B, I]
        assert scores_ug.requires_grad is False

        group_mask_zeros = torch.exp(group_mask).unsqueeze(2)  # [B, G, 1]
        scores_ug = torch.sigmoid(scores_ug)  # [B, G, 1]

        user_items_norm = torch.sum(user_items_norm * scores_ug * group_mask_zeros, dim=1) / group_mask_zeros.sum(1)
        user_group_loss = self.multinomial_loss(group_logits, user_items_norm)
        group_loss = self.multinomial_loss(group_logits, group_items_norm)

        return mi_loss, user_group_loss, group_loss

    def loss(self, group_logits, summary_embeds, scores_ug, group_mask, group_items, user_items, corrupted_user_items,
             device='cpu'):
        """ L_G + lambda L_UG + L_MI """
        mi_loss, user_group_loss, group_loss = self.infomax_group_loss(group_logits, summary_embeds, scores_ug,
                                                                       group_mask, group_items, user_items,
                                                                       corrupted_user_items, device)

        return group_loss + mi_loss + self.lambda_mi * user_group_loss