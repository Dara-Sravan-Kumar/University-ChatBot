#RunTheBot 

Install Anaconda of Python 3.7 distribution.

open Anaconda prompt(AC). 

create a virtual environment.
	``` conda create -n name_of_env python=3.7.6 ```

Follow the series of commands
``` conda activate name_of_env ```

``` conda install tensorflow ```

``` conda install ujson==1.35 ```

``` pip install rasa==1.9.5 ```

move to the bot directory using cd command

``` rasa train nlu ```

``` rasa train core ```

``` rasa train ```

``` rasa shell ``` to test your bot in the prompt.

all the trained model will be stored in bot/models directory

open server.py file & change the models, with model you have trained and save it.

In the AC run the command ``` python -m server.py ```

Now open the Home.html file in the templates folder in any web browser.

Experience The University_ChatBot. :)

If you want know more about RASA framework, its components and its backend working, Please refer to the link which has document prepared by @Dara Sravan Kumar, @Suggula Jagadeesh @Verra Dinesh 
link : https://docs.google.com/document/d/14d4y6EvjbOQKqstdEWVu-McCiQznKv2dCisKRQiF610/edit?usp=sharing
