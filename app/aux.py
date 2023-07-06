import difflib
import sqlite3

class PromptUtility:

    delimiter = "####"
    argument = "Environmentalists get science wrong as they are not committed to scientific principles. Therefore, environmentalists are biased and their reliability is questionable."

    # STEP 1: Deconstruct the claim:
    first_example = "A: Climate has changed naturally in the past, so current climate change is natural.\nP1: Climate has changed naturally in the past.\nP2: Climate is changing now.\nC: Therefore, current climate change is natural."
    first_template_string = """We are going to deconstruct climate misinformation to identify reasoning errors.\
    To do so, we will break down arguments into their starting assumptions or premises and their conclusions.\
    \nFor example, argument A has two premises, P1 and P2, and a conclusion, C: {example}
    Using this structure, please identify the premises and conclusion of the following argument delimited by {delimiter}. \
    {format_instructions}\n\
    {delimiter} {argument} {delimiter}
    """

    # STEP 2: Check validity:
    second_example = """
    Logically valid:
    A: 31,000 dissenting scientists prove there is no expert agreement on human-caused global warming"
    P1: A large proportion of people with science degrees dissent human-caused global warming.
    P2: People with science degreess are experts on climante change.
    C: There is no expert agreement on human-caused global warming.

    TRUE, This argument is logically valid, if it was true that a large proportion of science graduates dissented and all those science graduates were climate experts then yes, it would follow that there was no expert consensus on climate change.

    Logically invalid: 
    A: Climate has changed naturally in the past, so current climate change is natural.
    P1: Climate has changed naturally in the past.
    P2: Climate is changing now.
    C: Therefore, current climate change is natural.

    FALSE, This argument is logically invalid, just because the climate changed naturally in the past doesn't mean it's changing naturally now. """

    second_template_string = """Check if the argument delimited by {delimiter} is logically valid i.e. Does the conclusion follow from the premises?
    Assume that if all the premises are true, does it follow the conclusion is also true.
    Read the following examples before giving your answer, A: Argument, P#: Premises and C: Conclusion
    Examples: {example}

    {format_instructions}\n\

    {delimiter} {argument} {delimiter}
    """

    # STEP 3: Hidden premises:
    third_example = "A: Climate has changed naturally in the past, so current climate change is natural.\nP1: Climate has changed naturally in the past.\nP2: Climate is changing now.\nHP: If something wasn't a cause in the past, it can't be a cause now\nC: Therefore, current climate change is natural."

    third_template_string = """The conclusion of the argument delimited by {delimiter} doesn't follow from their premises, i.e. is logically invalid.
    We need to add an extra premise, an unstated assumption to make this argument logically valid. Follow the example bellow, A: Argument, P#: Premises, HP: Hidden premise C: Conclusion.
    Example: 
    {example}

    {format_instructions}\n\

    {delimiter} {argument} {delimiter}
    """

    # STEP 4: Check premises
    fourth_template_string = """Is the argument indicated by {delimiter} subject to any of the fallacies outlined in the provided table?\
    Thoroughly analyze each fallacy from the table, its definition and example before giving your answer.\
    Please ensure to only use the options from the table and refrain from introducing new ones.\
    If the argument is logically valid or it does not fall under any of the fallacies outlined, the response should be 'no fallacy'.\
    If the argument exhibits any of the fallacies, the response should consist of a list of these fallacies, separated by commas (for example: foo, bar, baz).\
    Please stick to the information requested and avoid including any extraneous details.\
    \n
    {table}
    \n
    {delimiter} {argument} {delimiter}
    """

    table = """TECHNIQUE,DEFINITION,EXAMPLE
    Ad Hominem,"Attacking a person/group instead of addressing their arguments.","Climate science can't be trusted because climate scientists are biased."
    Ambiguity,"Using ambiguous language in order to lead to a misleading conclusion.","Thermometer readings have uncertainty which means we don't know whether global warming is happening."
    Anecdote,"Using personal experience or isolated examples instead of sound arguments or compelling evidence.","The weather is cold today—whatever happened to global warming?"
    Blowfish,"Focusing on an inconsequential aspect of scientific research, blowing it out of proportion in order to distract from or cast doubt on the main conclusions of the research.","The hockey stick graph is invalid because it contains statistical errors."
    Bulk Fake Experts,"Citing large numbers of seeming experts to argue that there is no scientific consensus on a topic.","There is no expert consensus because 31,487 Americans with a science degree signed a petition saying humans aren't disrupting climate."
    Cherry Picking,"Carefully selecting data that appear to confirm one position while ignoring other data that contradicts that position.","Global warming stopped in 1998."
    Contradictory,"Simultaneously believing in ideas that are mutually contradictory.","The temperature record is fabricated by scientists… the temperature record shows cooling."
    Conspiracy Theory,"Proposing that a secret plan exists to implement a nefarious scheme such as hiding a truth.","The climategate emails prove that climate scientists have engaged in a conspiracy to deceive the public."
    Fake Debate,"Presenting science and pseudoscience in an adversarial format to give the false impression of an ongoing scientific debate.","Climate deniers should get equal coverage with climate scientists, providing a more balanced presentation of views."
    Fake Experts,"Presenting an unqualified person or institution as a source of credible information.","A retired physicist argues against the climate consensus, claiming the current weather change is just a natural occurrence."
    False Analogy,"Assuming that because two things are alike in some ways, they are alike in some other respect.","Climate sceptics are like Galileo who overturned the scientific consensus about geocentrism."
    False Choice,"Presenting two options as the only possibilities, when other possibilities exist.","CO2 lags temperature in the ice core record, proving that temperature drives CO2, not the other way around."
    False Equivalence (apples vs. oranges),"Incorrectly claiming that two things are equivalent, despite the fact that there are notable differences between them.","Why all the fuss about COVID when thousands die from the flu every year."
    Immune to evidence,"Re-interpreting any evidence that counters a conspiracy theory as originating from the conspiracy.","Those investigations finding climate scientists aren't conspiring were part of the conspiracy."
    Impossible Expectations,"Demanding unrealistic standards of certainty before acting on the science.","Scientists can't even predict the weather next week. How can they predict the climate in 100 years?"
    Magnified Minority,"Magnifying the significance of a handful of dissenting scientists to cast doubt on an overwhelming scientific consensus.","Sure, there's 97% consensus but Professor Smith disagrees with the consensus position."
    Misrepresentation,"Misrepresenting a situation or an opponent's position in such a way as to distort understanding.","They changed the name from 'global warming' to 'climate change' because global warming stopped happening."
    Moving Goalposts,"Demanding higher levels of evidence after receiving requested evidence.","Sea levels may be rising but they're not accelerating."
    Nefarious intent,"Assuming that the motivations behind any presumed conspiracy are nefarious.","Climate scientists promote the climate hoax because they're in it for the money."
    Overriding suspicion,"Having a nihilistic degree of scepticism towards the official account, preventing belief in anything that doesn't fit into the conspiracy theory.","Show me one line of evidence for climate change... oh, that evidence is faked!"
    Oversimplification,"Simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions.","CO2 is plant food so burning fossil fuels will be good for plants."
    Persecuted victim,"Perceiving and presenting themselves as the victim of organised persecution.","Climate scientists are trying to take away our freedom."
    Quote Mining,"Taking a person's words out-of-context in order to misrepresent their position.","Mike's trick… to hide the decline."
    Re-interpreting randomness,"Believing that nothing occurs by accident, so that random events are re-interpreted as being caused by the conspiracy.","NASA's satellite exploded? They must be trying to hide inconvenient data!"
    Red Herring,"Deliberately diverting attention to an irrelevant point to distract from a more important point.","CO2 is a trace gas so its warming effect is minimal."
    Single Cause,"Assuming a single cause or reason when there might be multiple causes or reasons.","Climate has changed naturally in the past so what's happening now must be natural."
    Slippery Slope,"Suggesting that taking a minor action will inevitably lead to major consequences.","If we implement even a modest climate policy, it will start us down the slippery slope to socialism and taking away our freedom."
    Slothful Induction,"Ignoring relevant evidence when coming to a conclusion.","There is no empirical evidence that humans are causing global warming."
    Something must be wrong,"Maintaining that something must be wrong and the official account is based on deception, even when specific parts of a conspiracy theory become untenable.","Ok, fine, 97% of climate scientists agree that humans are causing global warming, but that's just because they're toeing the party line."
    Straw Man,"Misrepresenting or exaggerating an opponent's position to make it easier to attack.","In the 1970s, climate scientists were predicting an ice age."
    """

    @staticmethod
    def print_dict(dictionary, argument):
        dictionary['A'] = argument
        keys = ['A'] + sorted(key for key in dictionary.keys() if key.startswith('P')) + ['C']
        argument = "\n".join(f"{key}: {dictionary[key]}" for key in keys)
        return argument
    
    @staticmethod
    def approximate_bool(value):
        true_representations = ['true', 'yes', 'on']
        false_representations = ['false', 'no', 'off']

        ratio_true = max(difflib.SequenceMatcher(None, value.lower(), true_val).ratio() for true_val in true_representations)
        ratio_false = max(difflib.SequenceMatcher(None, value.lower(), false_val).ratio() for false_val in false_representations)

        if ratio_true >= ratio_false:
            return True
        else:
            return False

    @classmethod
    def get_sample_argument(cls):
        return cls.argument

    @classmethod
    def get_delimiter(cls):
        return cls.delimiter
    
    @classmethod
    def get_first_example(cls):
        return cls.first_example
    
    @classmethod
    def get_first_template(cls):
        return cls.first_template_string
    
    @classmethod
    def get_second_example(cls):
        return cls.second_example
    
    @classmethod
    def get_second_template(cls):
        return cls.second_template_string
    
    @classmethod
    def get_third_example(cls):
        return cls.third_example
    
    @classmethod
    def get_third_template(cls):
        return cls.third_template_string
    
    @classmethod 
    def get_fourth_template(cls):
        return cls.fourth_template_string
    
    @classmethod
    def get_table(cls):
        return cls.table


class DBUtility:

    def __init__(self, database_path):
        self.database_path = database_path
        self.conn = sqlite3.connect(database_path)
        self.cursor = self.conn.cursor()

    def insert_premise(self, claims_id, premise, is_hidden, premise_identifier):
        # 1. insert premises on Pred_Premises table <- not hidden
        # 2. insert premises on Pred_Premises table <- hidden
            # claims_id -> claim id from claims table
            # premise -> premise text
            # is_hidden -> True or False
            # premise_identifier -> P1, P2, ... , Pn, HP1, ... HPn, C

        self.cursor.execute('''
        INSERT INTO Pred_Premises (claims_id, premise, is_hidden, premise_identifier) VALUES (?, ?, ?, ?)''',
        (claims_id, premise, is_hidden, premise_identifier))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_validity(self, claims_id, validity_txt, validity_bool):
        # 3. insert validity on LLM_Validity table
            # claims_id -> claim id from claims table
            # validity_txt -> reason text or None
            # validity_bool -> True or False

        self.cursor.execute('''
        INSERT INTO LLM_Validity (claims_id, validity_text, argument_validity) VALUES (?, ?, ?)''',
        (claims_id, validity_txt, validity_bool))
        self.conn.commit()

    def insert_fallacy(self, premise_id, fallacy_text, fallacy_validity=None):
        # 4. insert fallacies on Pred_Fallacies table
            # premise_id -> premise id from Pred_Premises table
            # fallacy_text -> identifyied fallacy
            # fallacy_validity -> reason why -> deprecated.

        self.cursor.execute('''
        INSERT INTO Pred_Fallacies (premise_id, fallacy_text, fallacy_validity) VALUES (?, ?, ?)''',
        (premise_id, fallacy_text, fallacy_validity))
        self.conn.commit()

    def get_claim(self, claim_id):
        # retrieves a specific claim from the Claims table
        self.cursor.execute('SELECT * FROM Claims WHERE claims_id = ?', (claim_id,))
        return self.cursor.fetchone()

    def get_all_claims(self):
        #retrieves all claims from the Claims table.
        self.cursor.execute('SELECT * FROM Claims')
        return self.cursor.fetchall()
    
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
