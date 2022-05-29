# [Token Surprisial Value](https://github.com/GeorgStin/Token-Surprisial-Value)

This is a small Python script for calculating of surpriasial value of tokens using a bigram-context. 

*Surprisial* of the event is the informational value of a particular event ([Attneave 1959](https://github.com/GeorgStin/Token-Surprisial-Value/edit/main/README.md#references), 6):

![H](http://www.sciweavers.org/tex2img.php?eq=H%20%3D%20log%20%5Cfrac%7B1%7D%7Bp%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

Without going into details, ***p*** for calculating of a token surpriasial in a certain context (the "context" is the previous two words or just "bigram") takes the following form:

		p = relative trigram frequency / relative bigram frequency

***

# Running Requirements

<li> Python 3.9</li>

***

# Files
## README.md
This file.

## korpus.txt
Here is a test corpus with three sentences. You can change this file and create your own corpus/text or you can copy a new txt-file to the folder with the script (*you need to change a variable in the script! see next section*).

## surprisial.py
The script is used to calculate the surprisial value of some token in a given corpus or text. The context (bigrams) and its relative frequency are used to calculating. Some special format of your corpus or text is not required for this script. Segmentation of corpus/text/string into sentences and padding are included.

- **Usage**: `python surprisial.py`
- **Input**: no special input is required (yet). To select your own corpus/text/string, you need to change the name of the variable `corpus` ("korpus.txt" by default). To select your own target token you need to change the name of the variable `target_token` ("men" by default).
- **Output**: you can see the results in your console. The output has the following format:
 
		Surprisal of "men" is: 1.584962500721156
		Context: sach de men		

***

# Padding
Sentences are padded only at the beginning of each sentence in the following format:
- for bigrams

		'^' '^'
- for trigrams

		'^' '^' '^'
To change the format of the padding you need to change the `bigram` and `trigram` variables respectively (in the `run_script` function).

***

# Performance Issues

Of course, this script will most likely not working as intended, since it was created for a specific homework assignment (just like this entire repository in general). However, if you invest a lot of time, you can make a script which can:
- adequately receive the task and target tokens from the console;
- tokenize sentences, considering abbreviations and complex syntax;
- change the conditions of padding and for example optionally pad sentences not only at the beginning, but also at the end;
- count surprisial value not only for a token that occurs only once in the whole corpus/text and choose in what context the token should be if it occurs more often than once;
- give an output in a format that can be useful for any purpose;
- etc.

***

# References
- *Attneave, F. (1959). Applications of information theory to psychology: A summary of basic concepts, methods, and results. Henry Holt.*
