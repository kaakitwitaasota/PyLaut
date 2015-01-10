class Phone(object):
    """
    Phones are the atomic unit of PyLaut. They are somewhere between acoustic
    phones and phonemes.
    
    They are a collection [dictionary + canonical order] of phonological features
    with extra structure to make manipulating them easier.
    """
    
    #the values features can take.
    #maybe we will change this to "+-0" or something, but i am storing it as a
    #class attribute for convenience

    _TRUE_FEATURE = True
    _FALSE_FEATURE = False
    _NULL_FEATURE = None
    _possible_feature_values = [_TRUE_FEATURE, _FALSE_FEATURE, _NULL_FEATURE]    
        
    def __init__(self):
        self.feature_set_name = None
        #self.feature_set is a canonical order for features, so features can be
        #set in one go as e.g. "+++--00+-"
        self.feature_set = list()
        self.features = dict()
        #representation of the Phone
        self.symbol = "0"
        
    def __repr__(self):
        """
        Actually there are many choices for the default representation, but for
        now it produces a string "[+feature] [-lol] [+dongs]"
        """
        output = []
        for feature in self.feature_set:
            if self.features[feature] == Phone._TRUE_FEATURE:
                output += ["[+{}]".format(feature)]
            elif self.features[feature] == Phone._FALSE_FEATURE:
                output += ["[-{}]".format(feature)]
            else:
                pass
        return " ".join(output)
        
    def load_set_feature_set(self,feature_set_file_name):
        """
        Loads a feature set from file, sets the Phone's feature set to it and 
        reinits self.features /!\ clearing any existing features /!\
        
        A feature set file is a plain text file, with the name of the feature set
        on the first line, with features given in []s each on its separate line
        """
        feature_set_raw = open(feature_set_file_name,"r").read().splitlines()
        feature_set_name = feature_set_raw[0]
        feature_set = [line for line in feature_set_raw if line and 
                       line[0] == "[" and line[-1] == "]" ]
        feature_set = [line[1:-1] for line in feature_set]
        
        #assign properties
        self.feature_set_name = feature_set_name
        self.feature_set = feature_set
        self.features = {x: None for x in self.feature_set}
        
    def set_features_from_ipa(self,ipa_char):
        """
        Takes Unicode IPA symbol and automagically assigns appropriate featural 
        values to Phone
        """
        pass
        
    def set_feature(self,feature_name,feature_value):
        """
        Sets the feature_name of the Phone to value feature_quality
        This ought not to be used directly, instead use  
        set_feature_true/false/null()
        """
        if not self.feature_set_name:
            raise Exception("Phone does not have a feature set initialised!")
        else:
            if feature_name not in self.features:
                raise Exception("Feature '{}' not found in Phone's "    
                                "feature set".format(feature_name))
            elif feature_value not in Phone._possible_feature_values:
                raise Exception("'{}' not a valid value for feature in "
                                "Phone".format(feature_value) )
            else:
                #do it
                self.features[feature_name] = feature_value

    def set_features_bool(self,feature_names,hey_boo):
        """
        Used by set_features_true/false/null
        
        hey_boo is the object that the feature is set to
        
        """
        #in case we are passed a string and not a list, so the loop can iterate
        #through it properly
        if type(feature_names) == str:
            feature_names = [feature_names]
        
        for feature_name in feature_names:
            self.set_feature(feature_name,hey_boo)
            
    def set_features_true(self,feature_names):
        """
        Sets the feature_name of the Phone to be true/+
        """
        self.set_features_bool(feature_names,Phone._TRUE_FEATURE)
    
    def set_features_false(self,feature_names):
        """
        Sets the feature_name of the Phone to be false/-
        """
        self.set_features_bool(feature_names,Phone._FALSE_FEATURE)
    
    def set_features_null(self,feature_names):
        """
        Sets the feature_name of the Phone to be null/0
        """
        self.set_features_bool(feature_names,Phone._NULL_FEATURE)
               
class MicroPhone(Phone):
    """
    MicroPhones are Phones which use the MICROMONOPHONE feature-set. For further 
    information, please refer to Phone.
    """
    def __init__(self):
        super().__init__()
        self.load_set_feature_set("micromonophone")

lol = MicroPhone()
lol.set_features_true(["consonantal","voice"])
lol.set_features_false("labial")

#the raw feature dict, don't do this
print(lol.features)
#lol.__repr__, do do this
print(lol)