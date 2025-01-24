'''
Problem:
We're going to build the beginnings of a markdown processor. Markdown is a markup language that allows you to easily create HTML.
We ll provide some sample input and desired output. 
Dont worry too much about edge cases, but feel free to ask if you re unsure or think there s something we ought to consider.

Part 1:  A markdown processor is capable of handling a multitude of string to html tag formats. For now, we just want to focus on supporting <p/>, <br/>, <blockquote/>, and <del/> tags.  

Input:
String input = "This is a paragraph with a soft\n" + "line break.\n\n" + 
               "This is another paragraph that has\n" + "> Some text that\n" + "> is in a\n" + "> block quote.\n\n" + 
			   "This is another paragraph with a ~~strikethrough~~ word.";  

paragraph1 = This is a paragraph with a soft\n line break.\n\n 
paragraph2 = This is another paragraph that has\n > Some text that\n > is in a\n > block quote.\n\n 
paragraph3 = This is another paragraph with a ~~strikethrough~~ word."


Expected Output:
"<p>This is a paragraph with a soft<br />line break.</p> 
<p>This is another paragraph that has <br />
<blockquote.>Some text that<br />is in a<br />
block quote</blockquote.> </p> <p>This is another paragraph with a
<del>strikethrough</del.> word.</p>"

<p>This is a paragraph with a soft<br/>line break.</p>
<p>This is another paragraph that has<br/>
<blockquote> Some text that<br/> is in a<br/>
 block quote.</blockquote></p><p>This is another paragraph with a <del>~strikethrough</del>~ word.</p>

conditions
\n -> break 
\n\n -> new paragraph
> -> enter into blockquote state
~~ -> enter into delete state


states 
- inBlockQuote
- inStrikeThrough
- inNewParagraph


partition string into paragraphs
split by \n\n

append <p>
for every paragraph, split by \n
    if first char of substring == >, enter into blockQuote state
    for every char in substring 
        if char == ~, invoke strikethrough method

        append char
    append <br />

append </p>


paragraph1 = This is a paragraph with a soft\n line break.\n\n 
    sentences = ["This is a paragraph with a soft", "line break."]

paragraph2 = This is another paragraph that has\n > Some text that\n > is in a\n > block quote.\n\n 
    sentences = ["This is another paragraph that has", 
                 "> Some text that", 
                 "> is in a",
                 "> block quote."
                ]
paragraph3 = This is another paragraph with a ~~strikethrough~~ word."
    sentences = ["This is another paragraph with a ~~strikethrough~~ word."]


    
states that the string could be in 
- block quote state
- strikethrough state

split string into paragraphs \n\n

algorithm
- loop through each paragraph
    - start with <p>
    - split the paragraph into sentences \n

    - loop through each sentence
        - check if sentence starts with >, if true, enter into block quote state

        - else, process regular sentence

        - add <br/>
    
    - if we are still in block quote state, end the block quote


processing block quote sentence algorithn
- if this is the start of the block quote, set blockquoteState = True and add <blockquote>
- for every char in sentence
    - 





'''
class Solution:
    def convert(self, input):
        self.output = ""
        self.inBlockQuoteState = False
        self.inStrikethroughState = False
        paragraphs = input.split("\n\n")

        for paragraph in paragraphs:
            self.output += "<p>"
            sentences = paragraph.split("\n")
            
            for i in range(len(sentences)):
                sentence = sentences[i]
                # check if first char is >
                if sentence[0] == ">":
                    self.processBlockQuoteSentence(sentence)

                else:
                    # end blockquote state
                    if self.inBlockQuoteState == True:
                        self.inBlockQuoteState = False
                        self.output += "</blockquote>"

                    self.processRegularSentence(sentence)

                if i < len(sentences) - 1:   
                    self.output += "<br/>"

            if self.inBlockQuoteState == True:
                self.inBlockQuoteState = False
                self.output += "</blockquote>"
            self.output += "</p>"

        return self.output

    def processBlockQuoteSentence(self, sentence):
        if self.inBlockQuoteState == False: 
            self.inBlockQuoteState = True
            # enter into blockquote state
            self.output += "<blockquote>"
            
        for j in range(len(sentence)):
            if j == 0 and self.inBlockQuoteState:
                # dont append the > 
                continue
            if j < len(sentence) - 1 and sentence[j:j+2] == "~~":
                if self.inStrikethroughState == False:
                    # enter into strikethrough state
                    inStrikethroughState = True
                    self.output += "<del>"
                else:
                    self.inStrikethroughState = False
                    self.output += "</del>"
            elif sentence[j] == "~" and sentence[j - 1] == "~":
                continue
            else:
                self.output += sentence[j]
    
    def processRegularSentence(self, sentence):
        for j in range(len(sentence)):
            if j < len(sentence) - 1 and sentence[j:j+2] == "~~":
                if self.inStrikethroughState == False:
                    # enter into strikethrough state
                    self.inStrikethroughState = True
                    self.output += "<del>"
                else:
                    self.inStrikethroughState = False
                    self.output += "</del>"
            elif sentence[j] == "~" and sentence[j - 1] == "~":
                continue
            else:
                self.output += sentence[j]


sln = Solution()
input = "This is a paragraph with a soft\n" + "line break.\n\n" + "This is another paragraph that has\n" + "> Some text that\n" + "> is in a\n" + "> block quote.\n\n" + "This is another paragraph with a ~~strikethrough~~ word.";  
print(sln.convert(input))