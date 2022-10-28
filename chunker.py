

import time
# import icecream
start = time.time()


# benepar is a "constituency parser" which identifies the grammar tree of a sentence, like this: (S (NP (NP (DT The) (NN time)) (PP (IN for)...)))
import benepar, spacy


# TO-DO: Check if creating the Doc has to happen after setting a custom attribute
nlp = spacy.load('en_core_web_md')
nlp.add_pipe("benepar", config={"model": "benepar_en3"})

# We don't want the length of a span to count things that aren't words. Define an attribute that counts only the number of words:

exclude = ("PUNCT", "SPACE")

def isword(token):
  return token not in exclude

def word_length(span):
  return sum(isword(token) for token in span)

from spacy.tokens import Span
# TO-DO: Check that this passes the Span object to the getter
Span.set_extension("word_length", getter=word_length)




# Runs the Spacy pipeline on the input sentence
text = "Mini scule is one of the smallest known species of frog, with a snout–vent length of 8.4 to 10.8 mm (0.33 to 0.43 in). It has bronze underparts, except for the groin and back of the thigh, which are brown. The underparts and upperparts have a distinct color border along the side of the body between the rib cage and hip. The side of the head is dark brown but becomes more flecked with cream towards the back. The upperparts are cream with brown flecks. The iris is red. The groin can have dark markings in some specimens, along with blacker flanks and a burnt umber crossband on the thighs and lower leg."
doc = nlp(text)




sentence = list(doc.sents)[-1]
limit = 5





def too_long(span):
  return span._.word_length > limit

def correct_size(span):
  return not too_long(span)







def get_chunks(*chunks):
      
      # I now realize how simple the recursion is
      
      # start at a node
      
      # iterate over the children, except you can do it without an awkward look ahead comparison
      
      # instead the parent node receives a tuple from each of its children
      
      # and the final command is ..... damn.
      
      # first of all if the parent receives 2 tuples from one node (due to nesting)
      
      # it of course has to be unpacked - its a tuple of tuples, so all thats passed are 2 tuples within
      
      # so the node returns the unpacked tuple of itself applied to each of its children
      
      # that specifically means pass each of the children
      # return chunk(*self.children)
      
      def combine(span1, span2):
        # is there any inclusive index? that would be wonderful.
        return sentence[span1.i : span2.i + 1]
      
      
      # this should just be renamed to an attribute called "span" or "chunk". if span.ischunk
      def short_enough(span):
        return limit > len(parent)
      
      
      
      # lists are mutable so maybe there's a recursion where you're changing the list but not returning it.
      # for element in list:
      #  # no it only works with an index
      # so i prefer a waterfall/cascade of list iterations, or tuple iterations
      # this is not correct, but its close....
      
      # remember, one form of recursion has to return tuples - one if they get combined, two if they do not.
      # which is precisely why the method has to unpack. 
      
      # second to last element calls "merge" on "next()" - its an iterator or a generator...
      # this is the only way to avoid using an index
      # thank god thats finally understood, holy shit. its basically proven.
      # or popping, soehow that hasnt felt as clean or elegant yet
      
      
      # spans is any number of tuples, but to pass those tuples, they have to be passed inside a tuple, so its pointless so unpack them. isnt that proven?
      def compress(spans):
        spans = iter(spans)
            
            
      # use the for loop to keep moving forward
      
      # one element awaits the value of next
      
      # compress(iter):
      #  
      
      # one more time
      # current_element
      # for element in tuple:
      #  1. grab the element: current_element = element
      #  2. 
      #  2. grab the next element by letting the loop continue. how????
      #  3. 
      
      
      
      def compress(spans)
      for span in spans:
        if short_enough(span):
          return span
        else:
          compress(spans.pop())
      
      def compress(spans):
        # could this return false if list is empty???
        while (span := spans.pop())
        # must take a list
        span = spans.pop()
        for span1 in spans:
          for span2 in spans.remove(span1):
            
      
      
      def compress(spans):
        span1, span2 = spans[0], spans[1]
        # as far as i know, the only reason to use unpacking is if you want to work with a tuple,
        # but the input is not a tuple for some reason.
        # think about that. is it more elegant to pass a generator that gets unpacked? it hoestly might be.
        # ut thats it, you dont have to return a tuple, you can pass an iterable instead. it feels purer indeed.
        (span1, span2) = 
        if short_enough(combine())
      
      def chunk(span1):
        # even better if this were a span attribute, span.sufficient_length
        if short_enough(span):
          return span
        else:
          # this is so ugly and inelegant, is there an itertools double iterator or something?
          
          # we can go to this boarding school i went to, it was a really formative experience for me
          children = span._.children
          # this just flattens the children to avoid excessive nesting tuples
          # rename chunk to span, it sounds way nicer.
          spans = [span for span in chunk(child) for child in children]
          # if the length of the combined span is small enough, return tuple addiiton. else, return tuple.
          
          # ITS RECURSION!!!!
          
          
          
          spans = [combine(span1, span2) for (span1, span2) in zip(spans, spans[1:]) if short_enough(combine(span1, span2)) else ]
          return chunks
        
      # # remember, this passes a bunch of chunks as a tuple. for loop is perfect for this.
        # parent.map(chunk, child)
          # i need something like filter... for each two, set addition if condition, but at the end you leaves remaining sets
          [(x,y) for x,y in zip(myList, myList[1:]) if y == 9]
          
          
          
            # chunk the child
            # but do what with it?
            # build a tuple 
            # "combine adjacent children"
            
      
      
      

  # pass in a tuple of sentence pieces
  for chunk in chunks:

    # Once a sentence piece is small enough, you've hit the bottom. Return it.
    if correct_size(chunk):

      return chunk

    # If a sentence piece is too long:
    if too_long(chunk):

      # break it up into its children and go through them one by one
      for sub_chunk in get_chunks(*chunk._.children):

        if chunk.word_length + sub_chunk.word_length <= limit:
          return sentence(chunk.i : sub_chunk.i + 1)
        # 


# old version - TBD(eleted)
"""
  for phrase in phrases:
    if too_long(phrase):
      # this returns a generator of the immediate grammatical sub-parts
      return get_chunks(*phrase._.children)
    else:
      return phrase
"""


root = sentence._.children

chunks = get_chunks(*root)

print(chunks)


end = time.time()

print(end - start)


