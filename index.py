import pandas as pd

columns=['FinInstrmGnlAttrbts.Id','FinInstrmGnlAttrbts.FullNm','FinInstrmGnlAttrbts.ClssfctnTp','FinInstrmGnlAttrbts.CmmdtyDerivInd','FinInstrmGnlAttrbts.NtnlCcy','Issr']

df=pd.read_csv("/content/drive/MyDrive/csv/DLTINS_20210117_01of01.xml",names=columns,header=None)

df.columns

df.head()

df.shape

df.to_csv("SteelEye_new.csv")