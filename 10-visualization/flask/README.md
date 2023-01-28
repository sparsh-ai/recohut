# Flask

### **Shazam API Song Analytics**

```python
#@markdown **Shazam API Song Analytics**
!git clone https://github.com/jonaxmc/title-song-recommender.git
%cd title-song-recommender
!pip install -r requirements.txt
!pip install -q colab-everything
from colab_everything import ColabFlask
ColabFlask('app.py') # Flask app path
```

### **CareerVillage Questions Recommender**

```python
#@markdown **Career Village Questions Recommender**
!git clone https://github.com/dataroot/Kaggle-CV.git
%cd Kaggle-CV
!pip install -r requirements.txt
import nltk
nltk.download('stopwords')
!pip install -q -U kaggle
!pip install --upgrade --force-reinstall --no-deps kaggle
!mkdir ~/.kaggle
!cp /content/drive/MyDrive/kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json
!kaggle competitions download -c data-science-for-good-careervillage
!mkdir data && unzip /content/data-science-for-good-careervillage.zip -d ./data
%tensorflow_version 1.x
!pip install 'h5py==2.10.0' --force-reinstall
!pip install -q colab-everything
from colab_everything import ColabFlask
ColabFlask('app.py') # Flask app path
```