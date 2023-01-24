-- Populate table folders_by_user:
---------------------------
INSERT INTO folders_by_user (username,label,color)
VALUES ('joe@datastax.com','inbox','black');
INSERT INTO folders_by_user (username,label,color)
VALUES ('joe@datastax.com','sent','black'); 
INSERT INTO folders_by_user (username,label,color)
VALUES ('joe@datastax.com','important','purple'); 
INSERT INTO folders_by_user (username,label,color)
VALUES ('jen@datastax.com','inbox','blue');
INSERT INTO folders_by_user (username,label,color)
VALUES ('jen@datastax.com','sent','blue'); 
INSERT INTO folders_by_user (username,label,color)
VALUES ('jen@datastax.com','spam','gray'); 
INSERT INTO folders_by_user (username,label,color)
VALUES ('jim@datastax.com','inbox','black');
INSERT INTO folders_by_user (username,label,color)
VALUES ('jim@datastax.com','sent','black'); 


-- Populate table unread_email_stats:
---------------------------
UPDATE unread_email_stats SET num_unread += 2
WHERE username = 'joe@datastax.com' AND label = 'inbox';
UPDATE unread_email_stats SET num_unread += 0
WHERE username = 'joe@datastax.com' AND label = 'sent'; 
UPDATE unread_email_stats SET num_unread += 1
WHERE username = 'joe@datastax.com' AND label = 'important'; 
UPDATE unread_email_stats SET num_unread += 1
WHERE username = 'jen@datastax.com' AND label = 'inbox';
UPDATE unread_email_stats SET num_unread += 0
WHERE username = 'jen@datastax.com' AND label = 'sent'; 
UPDATE unread_email_stats SET num_unread += 0
WHERE username = 'jen@datastax.com' AND label = 'spam'; 
UPDATE unread_email_stats SET num_unread += 1
WHERE username = 'jim@datastax.com' AND label = 'inbox';
UPDATE unread_email_stats SET num_unread += 0
WHERE username = 'jim@datastax.com' AND label = 'sent'; 


-- Populate table emails_by_user_folder:
-------------------------------------

INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('joe@datastax.com','inbox',8ae31dd0-d361-11ea-a40e-5dd6331dfc45,
        'jen@datastax.com','Documents',true);
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('joe@datastax.com','important',8ae31dd0-d361-11ea-a40e-5dd6331dfc45,
        'jen@datastax.com','Documents',true);
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('jim@datastax.com','inbox',8ae31dd0-d361-11ea-a40e-5dd6331dfc45,
        'jen@datastax.com','Documents',true);
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('jen@datastax.com','sent',8ae31dd0-d361-11ea-a40e-5dd6331dfc45,
        'jen@datastax.com','Documents',true);           

INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('jen@datastax.com','inbox',ea0a3f50-d361-11ea-a40e-5dd6331dfc45,
        'joe@datastax.com','Documents',false); 
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('jim@datastax.com','inbox',ea0a3f50-d361-11ea-a40e-5dd6331dfc45,
        'joe@datastax.com','Documents',false); 
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('joe@datastax.com','sent',ea0a3f50-d361-11ea-a40e-5dd6331dfc45,
        'joe@datastax.com','Documents',true);         


INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('joe@datastax.com','inbox',0b921770-d366-11ea-a881-13b3bf582948,
        'jen@datastax.com','Astra',false);   
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('joe@datastax.com','important',0b921770-d366-11ea-a881-13b3bf582948,
        'jen@datastax.com','Astra',false);              
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('jen@datastax.com','sent',0b921770-d366-11ea-a881-13b3bf582948,
        'jen@datastax.com','Astra',true); 
        
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('joe@datastax.com','inbox',21137dd0-d363-11ea-a40e-5dd6331dfc45,
        'jim@datastax.com','Lunch',false);              
INSERT INTO emails_by_user_folder (username,label,id,"from",subject,is_read)
VALUES ('jim@datastax.com','sent',21137dd0-d363-11ea-a40e-5dd6331dfc45,
        'jim@datastax.com','Lunch',true);         
        
        
-- Populate table emails:
------------------------------------------
INSERT INTO emails (id,"to","from",subject,body,attachments)
VALUES (8ae31dd0-d361-11ea-a40e-5dd6331dfc45,
        ['joe@datastax.com','jim@datastax.com'],'jen@datastax.com',
        'Documents','Hi Joe and Jim, ...',
        {'Budget.xlsx':530,'Presentation.pptx':2416});
INSERT INTO emails (id,"to","from",subject,body)
VALUES (ea0a3f50-d361-11ea-a40e-5dd6331dfc45,
        ['jen@datastax.com','jim@datastax.com'],'joe@datastax.com',
        'Documents','Hey Jen and Jim, ...');
INSERT INTO emails (id,"to","from",subject,body)
VALUES (0b921770-d366-11ea-a881-13b3bf582948,
        ['joe@datastax.com'],'jen@datastax.com',
        'Astra','Migrating to ...');
INSERT INTO emails (id,"to","from",subject,body)
VALUES (21137dd0-d363-11ea-a40e-5dd6331dfc45,
        ['joe@datastax.com'],'jim@datastax.com',
        'Lunch','Hello Joe, ...');
                

-- Populate table attachments:
-----------------------------------------
INSERT INTO attachments (email_id,filename,chunk_number,type,value)
VALUES (8ae31dd0-d361-11ea-a40e-5dd6331dfc45,'Budget.xlsx',1,'application/xlsx',textAsBlob('Chunk 1 stores this small file of size 530KB'));
INSERT INTO attachments (email_id,filename,chunk_number,type,value)
VALUES (8ae31dd0-d361-11ea-a40e-5dd6331dfc45,'Presentation.pptx',1,'application/pptx',textAsBlob('Chunk 1 stores the beginning 1000KB of this 2416KB file'));
INSERT INTO attachments (email_id,filename,chunk_number,type,value)
VALUES (8ae31dd0-d361-11ea-a40e-5dd6331dfc45,'Presentation.pptx',2,'application/pptx',textAsBlob('Chunk 2 stores the next 1000KB of this 2416KB file'));
INSERT INTO attachments (email_id,filename,chunk_number,type,value)
VALUES (8ae31dd0-d361-11ea-a40e-5dd6331dfc45,'Presentation.pptx',3,'application/pptx',textAsBlob('Chunk 3 stores the ending 416KB of this 2416KB file'));
