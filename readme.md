The supplementary material is as follows:

![Alt文本](MICCAI_2024.jpg)


---

* Install FLAIR library.
```angular2html
pip install -r requirements.txt
```

* RFMiD dataset is at [RFMid](https://ieee-dataport.org/documents/retinal-fundus-multi-disease-image-dataset-rfmid-20) 


* Prepare csv 
```angular2html
python prepare_partitions.py
```

* Pretrain
```angular2html
python main_pretrain.py --augment_description True --balance False --epochs 120 --batch_size 128 --num_workers 10
```

* Draw grad-cam
```angular2html
python grad_came_new.py
```

* draw t-sne
```angular2html
python tsne_model_load_new.py
```
