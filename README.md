# start a docker

* to start the docker paste:

sudo docker build --tag docname:1.0 .

and:

sudo docker run -p 8888:8888 docname:1.0 


# notebooks

The notebooks are in the notebooks folder:

**train_and_test.inyb**

Notebook, with comments, where models where trained and tested. You do not have to run it (but you can if you want - notice that models are already saved so the model save code is commented).
* notice that because of glove embeddigs are 1.8G, there could be a storage error while downloading from https://github.com/sdadas/polish-nlp-resources/releases/download/v1.0/glove.zip

**inference_new_data.ipynb**

It is the notebook where you can make an inference on totally new data (user input) - as an substitute of development.

Run all the code and enter a comment in the required field (make_single_comment_prediction). The model wil return an interpretation: wheather it is a neutral, positive or negative comment.


# data

data comes from PolEval 2019 competiton (task 6-2: http://2019.poleval.pl/index.php/tasks/task6)

Data link: http://2019.poleval.pl/task6/task_6-2.zip 

