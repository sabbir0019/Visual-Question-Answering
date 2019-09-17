#Data Information....


image_feature_size          = (700,400)
word_feature_size           = 300
max_length_questions        = 30

#Data FIle Locations....


data_img =                  'data/data_img.h5'
data_prepo =                'data/data_prepro.h5'
data_prepo_meta =           'data/data_prepro.json'
embedding_matrix_filename = 'data/ckpts/embeddings_%s.h5'%embedding_dim
glove_path =                'data/glove.6B.300d.txt'
train_questions_path =      'data/Questions_Train_mscoco/MultipleChoice_mscoco_train2014_questions.json'
val_annotations_path =      'data/validation_data/mscoco_val2014_annotations.json'
ckpt_model_weights_filename =    'data/ckpts/model_weights.h5'
model_weights_filename =    'data/model_weights.h5'



