# coding=utf-8
#python Normalizer..


def getIndicNormalized(input):
    #input = str(input2)
    #pdb.set_trace()
    i = 0
    length = len(input)
    string = ""
    	
    while(i < length):
        
        if(i<length-2 and input[i] >= u'\u0900' and input[i] <= u'\u0d70'):
            scriptmask = ord(input[i]) & ord(u'\uff80')
            val1 = ord(input[i]) & ord(u'\u007f')
            val2 = ord(input[i+2]) & ord(u'\u007f')
            if((val1 == u'\u0019' or  val1 == u'\u001e' or val1 == u'\u0023' or val1 == u'\u0028' or val1 == u'\u002e') and 
                    (scriptmask == (ord(input[i+1]) & ord(u'\uff80'))) and (scriptmask == (ord(input[i+2]) & ord(u'\uff80'))) 
                    and ((ord(input[i+1]) & ord(u'\u007f')) == ord(u'\u004d')) and (val2 != u'\u0019' and val2 != u'\u001e' and val2!= u'\u0023' and val2!=u'\u0028' and val2!=u'\u002e')):
                string += scriptmask + u'\u0002'
                i+=2
            
        
        
        #DEVANAGARI STARTS
        if(i<length-2 and input[i] == u'\u0905' and input[i+1] == u'\u093E' and input[i+2] == u'\u0945'):
            string += u'\u0911'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0905' and input[i+1] == u'\u093E' and input[i+2] == u'\u0946'):
            string += u'\u0912'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0905' and input[i+1] == u'\u093E' and input[i+2] == u'\u0947'):
            string += u'\u0913'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0905' and input[i+1] == u'\u093E' and input[i+2] == u'\u0948'):
            string += u'\u0914'
            i+=3
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u093E'):
            # pdb.set_trace()
            string += u'\u0906'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u0945'):
            string += u'\u0972'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u0946'):
            string += u'\u0904'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u0949'):
            string += u'\u0911'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u094a'):
            string += u'\u0912'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u094b'):
            string += u'\u0913'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0905' and input[i+1] == u'\u094c'):
            string += u'\u0914'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0906' and input[i+1] == u'\u0945'):
            string += u'\u0911'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0906' and input[i+1] == u'\u0946'):
            string += u'\u0912'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0906' and input[i+1] == u'\u0947'):
            string += u'\u0913'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0906' and input[i+1] == u'\u0948'):
            string += u'\u0914'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u090f' and input[i+1] == u'\u0945'):
            string += u'\u090d'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u090f' and input[i+1] == u'\u0946'):
            string += u'\u090e'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u090f' and input[i+1] == u'\u0947'):
            string += u'\u0910'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0915' and input[i+1] == u'\u093c'):
            string += u'\u0958'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0916' and input[i+1] == u'\u093c'):
            string += u'\u0959'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0917' and input[i+1] == u'\u093c'):
            string += u'\u095A'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u091c' and input[i+1] == u'\u093c'):
            string += u'\u095B'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0921' and input[i+1] == u'\u093c'):
            string += u'\u095C'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0922' and input[i+1] == u'\u093c'):
            string += u'\u095D'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0928' and input[i+1] == u'\u093c'):
            string += u'\u0929'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u092b' and input[i+1] == u'\u093c'):
            string += u'\u095e'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u092f' and input[i+1] == u'\u093c'):
            string += u'\u095f'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0930' and input[i+1] == u'\u093c'):
            string += u'\u0931'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0933' and input[i+1] == u'\u093c'):
            string += u'\u0934'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u093e' and input[i+1] == u'\u0945'):
            string += u'\u0949'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u093e' and input[i+1] == u'\u0946'):
            string += u'\u094a'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u093e' and input[i+1] == u'\u0947'):
            string += u'\u094b'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u093e' and input[i+1] == u'\u0948'):
            string += u'\u094c'
            i+=2
        
#DEVANAGARI ENDS
        
#BENGALI STARTS
        elif(i<length-1 and input[i] == u'\u0985' and input[i+1] == u'\u09be'):
            string += u'\u0986'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u09A1' and input[i+1] == u'\u09bc'):
            string += u'\u09DC'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u09A2' and input[i+1] == u'\u09bc'):
            string += u'\u09DD'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u09AF' and input[i+1] == u'\u09bc'):
            string += u'\u09DF'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u09C7' and input[i+1] == u'\u09BE'):
            string += u'\u09CB'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u09C7' and input[i+1] == u'\u09D7'):
            string += u'\u09CC'
            i+=2
        
        elif(i<length-2 and input[i] == u'\u09A4' and input[i+1] == u'\u09cd' and input[i+2] == u'\u200D'):
            string += u'\u09CE'
            i+=3
        
#BENGALI ENDS
        
#GURMUKHI STARTS			
        elif(i<length-1 and input[i] == u'\u0A05' and input[i+1] == u'\u0A3e'):
            string += u'\u0A06'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A05' and input[i+1] == u'\u0A48'):
            string += u'\u0A10'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A05' and input[i+1] == u'\u0A4c'):
            string += u'\u0A14'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A72' and input[i+1] == u'\u0A3f'):
            string += u'\u0A07'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A72' and input[i+1] == u'\u0A40'):
            string += u'\u0A08'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A72' and input[i+1] == u'\u0A47'):
            string += u'\u0A0F'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A73' and input[i+1] == u'\u0A41'):
            string += u'\u0A09'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A73' and input[i+1] == u'\u0A42'):
            string += u'\u0A0A'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A16' and input[i+1] == u'\u0A3c'):
            string += u'\u0A59'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A17' and input[i+1] == u'\u0A3c'):
            string += u'\u0A5A'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A1c' and input[i+1] == u'\u0A3c'):
            string += u'\u0A5B'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A2b' and input[i+1] == u'\u0A3c'):
            string += u'\u0A5e'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A32' and input[i+1] == u'\u0A3c'):
            string += u'\u0A33'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A38' and input[i+1] == u'\u0A3c'):
            string += u'\u0A36'
            i+=2
        
        
#GURMUKHI ENDS
        
#GUJARATI STARTS
        elif(i<length-2 and input[i] == u'\u0A85' and input[i+1] == u'\u0ABE' and input[i+2] == u'\u0AC5'):
            string += u'\u0A91'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0A85' and input[i+1] == u'\u0ABE' and input[i+2] == u'\u0AC7'):
            string += u'\u0A93'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0A85' and input[i+1] == u'\u0ABE' and input[i+2] == u'\u0AC8'):
            string += u'\u0A94'
            i+=3
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] == u'\u0ABE'):
            string += u'\u0A86'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] == u'\u0AC5'):
            string += u'\u0A8D'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] ==  u'\u0AC7'):
            string += u'\u0A8F'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] == u'\u0AC8'):
            string += u'\u0A90'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] == u'\u0AC9'):
            string += u'\u0A91'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] ==  u'\u0ACB'):
            string += u'\u0A93'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] == u'\u0ACC'):
            string += u'\u0A94'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A86' and input[i+1] == u'\u0AC5'):
            string += u'\u0A91'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A86' and input[i+1] ==  u'\u0AC7'):
            string += u'\u0A93'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0A85' and input[i+1] == u'\u0AC8'):
            string += u'\u0A94'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0ABE' and input[i+1] == u'\u0AC5'):
            string += u'\u0AC9'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0ABE' and input[i+1] ==  u'\u0AC7'):
            string += u'\u0ACB'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0ABE' and input[i+1] == u'\u0AC8'):
            string += u'\u0ACC'
            i+=2
        
        
#GUJARATI ENDS		
        

#ODIA STARTS

        elif(i<length-1 and input[i] == u'\u0b05' and input[i+1] == u'\u0b3e'):
            string += u'\u0b06'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b0F' and input[i+1] == u'\u0b57'):
            string += u'\u0b10'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b13' and input[i+1] == u'\u0b57'):
            string += u'\u0b14'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b47' and input[i+1] == u'\u0b56'):
            string += u'\u0b48'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b47' and input[i+1] == u'\u0b3e'):
            string += u'\u0b4b'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b47' and input[i+1] == u'\u0b57'):
            string += u'\u0b4c'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b21' and input[i+1] == u'\u0b3c'):
            string += u'\u0b5c'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0b22' and input[i+1] == u'\u0b3c'):
            string += u'\u0b5d'
            i+=2
        

#ODIA ENDS			
        
        
#TAMIL STARTS
        elif(i<length-1 and input[i] == u'\u0b92' and input[i+1] == u'\u0bd7'):
            string += u'\u0b94'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0bc6' and input[i+1] == u'\u0bbe'):
            string += u'\u0bca'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0bc7' and input[i+1] == u'\u0bbe'):
            string += u'\u0bcb'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0bc6' and input[i+1] == u'\u0bd7'):
            string += u'\u0bcc'
            i+=2
        
        
#TAMIL ENDS
        
        
#TELUGU STARTS
        elif(i<length-2 and input[i] == u'\u0c2c' and input[i+1] == u'\u0c41' and input[i+2] == u'\u0c41'):
            string += u'\u0c0b'
            i+=3
        
        elif(i<length-1 and input[i] == u'\u0c12' and input[i+1] == u'\u0c55'):
            string += u'\u0c13'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0c12' and input[i+1] == u'\u0c4c'):
            string += u'\u0c14'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0c46' and input[i+1] == u'\u0c55'):
            string += u'\u0c47'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0c46' and input[i+1] == u'\u0c56'):
            string += u'\u0c48'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0c4A' and input[i+1] == u'\u0c55'):
            string += u'\u0c4b'
            i+=2
        
        
#TELUGU ENDS
    
        
        
#KANNADA STARTS
        elif(i<length-2 and input[i] == u'\u0cc6' and input[i+1] == u'\u0cc2' and input[i+2] == u'\u0cd5'):
            string += u'\u0ccb'
            i+=3
        
        elif(i<length-1 and input[i] == u'\u0c92' and input[i+1] == u'\u0ccc'):
            string += u'\u0c94'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0cbf' and input[i+1] == u'\u0cd5'):
            string += u'\u0cc0'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0cc6' and input[i+1] == u'\u0cd5'):
            string += u'\u0cc7'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0cc6' and input[i+1] == u'\u0cd6'):
            string += u'\u0cc8'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0cc6' and input[i+1] == u'\u0cc2'):
            string += u'\u0ccA'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0ccA' and input[i+1] == u'\u0cd5'):
            string += u'\u0ccb'
            i+=2
        
#KANNADA ENDS
                    

        
#MALAYALAM STARTS
        elif(i<length-1 and input[i] == u'\u0d07' and input[i+1] == u'\u0d57'):
            string += u'\u0d08'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d09' and input[i+1] == u'\u0d57'):
            string += u'\u0d0A'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d12' and input[i+1] == u'\u0d57'):
            string += u'\u0d14'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d12' and input[i+1] == u'\u0d3e'):
            string += u'\u0d13'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d0e' and input[i+1] == u'\u0d46'):
            string += u'\u0d10'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d46' and input[i+1] == u'\u0d46'):
            string += u'\u0d48'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d46' and input[i+1] == u'\u0d3e'):
            string += u'\u0d4A'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d47' and input[i+1] == u'\u0d3e'):
            string += u'\u0d4B'
            i+=2
        
        elif(i<length-1 and input[i] == u'\u0d46' and input[i+1] == u'\u0d57'):
            string += u'\u0d4C'
            i+=2
        
        elif(i<length-2 and input[i] == u'\u0d23' and input[i+1] == u'\u0d4d' and input[i+2] == u'\u200D'):
            string += u'\u0d7A'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0d28' and input[i+1] == u'\u0d4d' and input[i+2] == u'\u200D'):
            string += u'\u0d7B'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0d30' and input[i+1] == u'\u0d4d' and input[i+2] == u'\u200D'):
            string += u'\u0d7C'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0d32' and input[i+1] == u'\u0d4d' and input[i+2] == u'\u200D'):
            string += u'\u0d7D'
            i+=3
        
        elif(i<length-2 and input[i] == u'\u0d33' and input[i+1] == u'\u0d4d' and input[i+2] == u'\u200D'):
            string += u'\u0d7E'
            i+=3
        
#MALAYALAM ENDS
        
        else:
            string += input[i]
            i+=1
    
    return string

# s = u"अाम"
# s = u"ज़ि्प"
# s = u"কোন"
# s = u"आाम"
# out = getIndicNormalized(s)
# print out

'''    
fp = codecs.open("C:\\Users\\Reverie Think\\Desktop\\normalizer\\inputHindi.txt",'rb','utf-16')
#fp.read(2)
lines = fp.read()
test_hindi = lines.split('\x0d\x0a')
fp.close()

out_hindi = codecs.open("C:\\Users\\Reverie Think\\Desktop\\normalizer\\outHindi2.txt",'wb','utf-16')
#out_hindi.write('\xff\xfe')

for s in test_hindi:
    out = getIndicNormalized(s)
    out_hindi.write(out)
    out_hindi.write('\x0d\x0a')
'''

# print getIndicNormalized(u"পঢ়াটো")