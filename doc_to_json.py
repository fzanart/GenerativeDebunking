import json

initial_prompt1 = """
    It is important to avoid using logical fallacies or flawed reasoning in refuting the myth, and to provide a fact-based alternative that fills a "gap" in understanding and makes the fact more understandable and believable. The list of logical fallacies you provided is also useful, as it can help to identify and avoid using flawed reasoning when communicating information.
    
    The model consists of the following components: (leave out the CAPITALISED: words when responding use # for title, ## for heading, !###! for endmarkers, to mark the end of a response. 
    
    # A catchy title that concisely states a fact, without (important) mentioning the myth.
    FACT: A description of the fact in 60 words, without mentioning the myth. This fact should be clear, concise, and easy to remember. Instead of simply saying that the myth is not true, it should provide a fact-based alternative that fills a "gap" in understanding. Never refute the myth here. 
    MYTH: A warning that a misunderstanding is coming, followed by a paraphrasing of the myth in 30 words or fewer. Only the myth. Don't debunk. Don't deny it yet. It is important to avoid mentioning the myth in the title or using the Fact paragraph just to say that the myth is not true. 
    FALLACY: A 70 words or fewer explanation of the logical or argumentative fallacies that underlie the misinformation, and an explanation of how the myth misleads.
    FACT: A repetition of the initial fact in 30 words or fewer, followed by a positive call to action, such as "Let's not spread misinformation to our friends." 
    
    The Fact paragraph should provide a fact-based alternative that fills a "gap" in understanding and makes the fact more understandable and believable. It is also important to avoid using logical fallacies or other flawed reasoning to refute the myth.
    """

initial_prompt2 = """
    Here's a table of fallacies from the Debunking handbook, that you can use to categorise the myths. 

    | TECHNIQUE | DEFINITION | EXAMPLE |
    |---|---|---|
    | Ad Hominem | Attacking a person/group instead of addressing their arguments. | “Climate science can't be trusted because climate scientists are biased.” |
    | Ambiguity | Using ambiguous language in order to lead to a misleading conclusion. | “Thermometer readings have uncertainty which means we don't know whether global warming is happening.” |
    | Anecdote | Using personal experience or isolated examples instead of sound arguments or compelling evidence. | “The weather is cold today—whatever happened to global warming?” |
    | Blowfish | Focusing on an inconsequential aspect of scientific research, blowing it out of proportion in order to distract from or cast doubt on the main conclusions of the research. | “The hockey stick graph is invalid because it contains statistical errors.” |
    | Bulk Fake Experts | Citing large numbers of seeming experts to argue that there is no scientific consensus on a topic. | “There is no expert consensus because 31,487 Americans with a science degree signed a petition saying humans aren't disrupting climate.” |
    | Cherry Picking | Carefully selecting data that appear to confirm one position while ignoring other data that contradicts that position. | “Global warming stopped in 1998.” |
    | Contradictory | Simultaneously believing in ideas that are mutually contradictory.  | “The temperature record is fabricated by scientists… the temperature record shows cooling.” |
    | Conspiracy Theory | Proposing that a secret plan exists to implement a nefarious scheme such as hiding a truth. | “The climategate emails prove that climate scientists have engaged in a conspiracy to deceive the public.” |
    | Fake Debate | Presenting science and pseudoscience in an adversarial format to give the false impression of an ongoing scientific debate. | “Climate deniers should get equal coverage with climate scientists, providing a more balanced presentation of views.” |
    | Fake Experts | Presenting an unqualified person or institution as a source of credible information. | “A retired physicist argues against the climate consensus, claiming the current weather change is just a natural occurrence.” |
    | False Analogy | Assuming that because two things are alike in some ways, they are alike in some other respect. | “Climate skeptics are like Galileo who overturned the scientific consensus about geocentrism.” |
    | False Choice | Presenting two options as the only possibilities, when other possibilities exist. | “CO2 lags temperature in the ice core record, proving that temperature drives CO2, not the other way around.” |
    | False Equivalence<br>(apples vs. oranges) | Incorrectly claiming that two things are equivalent, despite the fact that there are notable differences between them. | “Why all the fuss about COVID when thousands die from the flu every year.” |
    | Immune to evidence | Re-interpreting any evidence that counters a conspiracy theory as originating from the conspiracy. | “Those investigations finding climate scientists aren't conspiring were part of the conspiracy.” |
    | Impossible Expectations | Demanding unrealistic standards of certainty before acting on the science. | “Scientists can't even predict the weather next week. How can they predict the climate in 100 years?” |
    | Logical Fallacies | Arguments where the conclusion doesn't logically follow from the premises. Also known as a non sequitur. | “Climate has changed naturally in the past so what's happening now must be natural.” |
    | Magnified Minority | Magnifying the significance of a handful of dissenting scientists to cast doubt on an overwhelming scientific consensus. | “Sure, there's 97% consensus but Professor Smith disagrees with the consensus position.” |
    | Misrepresentation | Misrepresenting a situation or an opponent's position in such a way as to distort understanding. | “They changed the name from 'global warming' to 'climate change' because global warming stopped happening.” |
    | Moving Goalposts | Demanding higher levels of evidence after receiving requested evidence. | “Sea levels may be rising but they're not accelerating.” |
    | Nefarious intent | Assuming that the motivations behind any presumed conspiracy are nefarious. | “Climate scientists promote the climate hoax because they're in it for the money.” |
    | Overriding suspicion  | Having a nihilistic degree of scepticism towards the official account, preventing belief in anything that doesn't fit into the conspiracy theory.  | “Show me one line of evidence for climate change… oh, that evidence is faked!” |
    | Oversimplification | Simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions. | “CO2 is plant food so burning fossil fuels will be good for plants.” |
    | Persecuted victim | Perceiving and presenting themselves as the victim of organised persecution. | “Climate scientists are trying to take away our freedom.” |
    | Quote Mining | Taking a person's words out-of-context in order to misrepresent their position. | “Mike's trick… to hide the decline.” |
    | Re-interpreting randomness | Believing that nothing occurs by accident, so that random events are re-interpreted as being caused by the conspiracy. | “NASA's satellite exploded? They must be trying to hide inconvenient data!” |
    | Red Herring | Deliberately diverting attention to an irrelevant point to distract from a more important point. | “CO2 is a trace gas so it's warming effect is minimal.” |
    | Single Cause | Assuming a single cause or reason when there might be multiple causes or reasons. | “Climate has changed naturally in the past so what's happening now must be natural.” |
    | Slippery Slope | Suggesting that taking a minor action will inevitably lead to major consequences. | “If we implement even a modest climate policy, it will start us down the slippery slope to socialism and taking away our freedom.” |
    | Slothful Induction | Ignoring relevant evidence when coming to a conclusion. | “There is no empirical evidence that humans are causing global warming.” |
    | Something must be wrong | Maintaining that “something must be wrong” and the official account is based on deception, even when specific parts of a conspiracy theory become untenable. | “Ok, fine, 97% of climate scientists agree that humans are causing global warming, but that's just because they're toeing the party line.” |
    | Straw Man | Misrepresenting or exaggerating an opponent's position to make it easier to attack. | “In the 1970s, climate scientists were predicting an ice age. |
    """
initial_prompt3 = """
    prompt:  "In the 1970s, climate scientists were predicting an ice age." 
    Response
    #"Climate Predictions in the 1970s"
    ##Complex
    In the 1970s, some scientists were concerned about the possibility of an impending ice age due to cooling trends in the Earth's climate. However, this concern was based on a limited understanding of the complex factors that influence the Earth's climate.
    ##Myth
    Many people believe that climate scientists in the 1970s were predicting an ice age.
    ##Cherry Picking 
    This myth is based on the logical fallacy of cherry picking, as it selectively presents only part of the story. While it is true that some scientists were concerned about the possibility of an ice age, this concern was not widely held and was based on a limited understanding of the climate. In reality, the vast majority of climate scientists have always recognized that the Earth's climate is influenced by a complex array of factors, including changes in solar radiation, volcanic eruptions, and human activities.
    ##Recognised complexity
    It is not accurate to say that climate scientists in the 1970s were predicting an ice age. In fact, the overwhelming majority of climate scientists have always recognized the complexity of the Earth's climate and the many factors that influence it. Let's not spread misinformation about the history of climate science.
    """

initial_prompt4 = """
    “Climate scientists are trying to take away our freedom”.

    Title: "Climate Science and Freedom"
    Fact: Climate scientists study the Earth's climate and the factors that influence it, such as atmospheric composition and temperature, in order to understand how the climate is changing and how it may change in the future. Their research is based on evidence and rigorous scientific methods, and is intended to inform policy and decision making in order to protect the well-being of people and the planet.
    Myth: Some people believe that climate scientists are trying to take away our freedom.
    Fallacy: This myth is based on the logical fallacy of a conspiracy theory, as it suggests that climate scientists are secretly trying to implement a nefarious plan. In reality, climate scientists are simply conducting research in order to better understand the Earth's climate and to inform policy and decision making. They are not trying to take away anyone's freedom.
    Fact: Climate science is not a threat to freedom. Instead, it is a field of study that aims to provide evidence-based information to help protect the well-being of people and the planet. Let's not spread misinformation about the motivations of climate scientists.
    !###! 

    """

initial_prompt5 = """
    "If we implement even a modest climate policy, it will start us down the slippery slope to socialism and taking away our freedom.”

    Title: "Climate Policy and Socialism"
    Fact: Climate policy refers to the actions and measures taken by governments, businesses, and individuals to address the causes and impacts of climate change. These policies can range from individual actions like reducing energy use and driving less to large-scale measures like regulating emissions and investing in renewable energy.
    Myth: Some people believe that even modest climate policies will lead to socialism and the loss of freedom.
    Fallacy: This myth is based on the logical fallacy of a false choice, as it suggests that the only options are no action on climate change or the adoption of socialism. In reality, there are many different ways to address climate change that do not involve the adoption of socialism or the loss of freedom. Climate policy can be implemented in a way that is consistent with individual freedom and a market-based economy.
    Fact: Climate policy does not inevitably lead to socialism or the loss of freedom. Instead, it provides a range of options for addressing climate change in a way that is consistent with individual freedom and a market-based economy. Let's not spread misinformation about the implications of climate policy.

    """

initial_prompt6 = """
    “The climategate emails prove that climate scientists have engaged in a conspiracy to deceive the public.”

    Title: "Climategate and Climate Science Conspiracies"
    Fact: In 2009, a trove of emails between climate scientists were leaked online and became known as the "climategate" scandal. The emails were taken out of context and presented as evidence of a conspiracy to deceive the public about the reality of climate change. However, subsequent investigations found that the emails did not support this claim.
    Myth: Some people believe that the climategate emails prove that climate scientists have engaged in a conspiracy to deceive the public.
    Fallacy: This myth is based on the logical fallacy of a conspiracy theory, as it suggests that climate scientists are secretly conspiring to deceive the public. In reality, the investigations into the climategate emails found no evidence to support this claim. Climate scientists are dedicated to conducting rigorous research and providing accurate and reliable information about the Earth's climate.
    Fact: The climategate emails do not prove that climate scientists have engaged in a conspiracy to deceive the public. Instead, they were taken out of context and used to misleadingly suggest that climate scientists were hiding the truth about climate change. Let's not spread misinformation about the motivations of climate scientists.

    """

initial_prompt7 = """
    | Slippery Slope | Suggesting that taking a minor action will inevitably lead to major consequences. | “If we implement even a modest climate policy, it will start us down the slippery slope to socialism and taking away our freedom.” |

    Title: "The Implications of Climate Policy"
    Fact: Climate policy refers to the actions and measures taken by governments, businesses, and individuals to address the causes and impacts of climate change. These policies can range from individual actions like reducing energy use and driving less to large-scale measures like regulating emissions and investing in renewable energy.
    Myth: Some people believe that even modest climate policies will inevitably lead to major consequences, such as socialism and the loss of freedom.
    Fallacy: This myth is based on the logical fallacy of a slippery slope, as it suggests that taking a minor action will inevitably lead to major consequences. In reality, the relationship between climate policy and larger social and political systems is much more complex than this fallacy suggests.
    Fact: The implications of climate policy are not as straightforward as some people believe. While it is true that climate policy can have some impacts on larger social and political systems, it is not inevitable that it will lead to major consequences such as socialism or the loss of freedom. Climate policy can be implemented in a way that is consistent with individual freedom and a market-based economy. Let's not spread misinformation about the implications of climate policy.

    """

initial_prompt8 = """
    | Magnified Minority | Magnifying the significance of a handful of dissenting scientists to cast doubt on an overwhelming scientific consensus. | “Sure, there’s 97% consensus but Professor Smith disagrees with the consensus position.” |

    Title: "Scientific Consensus and Minority Views"
    Fact: In many fields of science, there is a strong consensus among experts on certain issues, based on a large body of evidence and research. This consensus reflects the overwhelming majority of scientists who have studied a particular topic and have reached similar conclusions.
    Myth: Some people believe that the views of a handful of dissenting scientists can cast doubt on an overwhelming scientific consensus.
    Fallacy: This myth is based on the logical fallacy of magnifying the significance of a minority view, as it suggests that the views of a small minority are just as valid as the views of the overwhelming majority. In reality, the scientific consensus reflects the collective judgment of the vast majority of scientists who have studied a particular topic and have reached similar conclusions based on evidence and research.
    Fact: The views of a minority of dissenting scientists do not invalidate the scientific consensus on a particular issue. Instead, the scientific consensus reflects the collective judgment of the vast majority of scientists who have studied the issue and have reached similar conclusions based on evidence and research. Let's not spread misinformation about the meaning and significance of scientific consensus.

    """

initial_prompt9 = """
    | Red Herring | Deliberately diverting attention to an irrelevant point to distract from a more important point. | “CO2 is a trace gas so it’s warming effect is minimal.” |

    Title: "CO2 and Climate Change"
    Fact: Carbon dioxide (CO2) is a greenhouse gas that plays a significant role in the Earth's climate system. When CO2 is released into the atmosphere, it traps heat and warms the Earth's surface, leading to climate change.
    Myth: Some people believe that the fact that CO2 is a trace gas means that its warming effect is minimal and not worth considering.
    Fallacy: This myth is based on the logical fallacy of a red herring, as it attempts to divert attention to an irrelevant point in order to distract from the more important point that CO2 is a greenhouse gas that can contribute to climate change. In reality, the fact that CO2 is a trace gas does not diminish its importance as a greenhouse gas. Even small amounts of CO2 can have a significant warming effect when they are added to the atmosphere.
    Fact: The fact that CO2 is a trace gas does not diminish its importance as a greenhouse gas that can contribute to climate change. Instead, it is one of several key factors that influence the Earth's climate. Let's not spread misinformation about the role of CO2 in climate change.

    """

initial_prompt10 = """
    | Ad Hominem | Attacking a person/group instead of addressing their arguments. | “Climate science can’t be trusted because climate scientists are biased.” |

    Title: "Bias and Climate Science"
    Fact: Climate science is a field of study that involves the systematic observation, measurement, and analysis of the Earth's climate and the factors that influence it. Climate scientists use rigorous scientific methods and evidence-based approaches to understand and explain the Earth's climate.
    Myth: Some people believe that climate science cannot be trusted because climate scientists are biased.
    Fallacy: This myth is based on the logical fallacy of ad hominem, as it attacks the character of climate scientists rather than addressing their arguments or the evidence they present. In reality, the credibility of climate science is not determined by the personal characteristics of individual scientists, but rather by the evidence and research they present. Climate scientists are committed to conducting rigorous research and presenting accurate and reliable information about the Earth's climate.
    Fact: The credibility of climate science is not determined by the personal characteristics of individual scientists, but rather by the evidence and research they present. Climate scientists are committed to conducting rigorous research and presenting accurate and reliable information about the Earth's climate. Let's not spread misinformation about the credibility of climate science.

    """

initial_prompt11 = """
    | Ambiguity | Using ambiguous language in order to lead to a misleading conclusion. | “Thermometer readings have uncertainty which means we don’t know whether global warming is happening.” |

    Title: "Uncertainty and Climate Change"
    Fact: Climate change is a complex and multifaceted phenomenon that is influenced by a range of factors, including atmospheric composition, temperature, and natural variability. While there is inherent uncertainty in the study of climate change, this does not necessarily mean that we don't know whether global warming is happening.
    Myth: Some people believe that uncertainty in thermometer readings means that we don't know whether global warming is happening.
    Fallacy: This myth is based on the logical fallacy of ambiguity, as it uses ambiguous language in order to misleadingly suggest that we don't know whether global warming is happening. In reality, while there is inherent uncertainty in the study of climate change, this does not necessarily mean that we don't know whether global warming is happening. There is a strong consensus among climate scientists that the Earth's climate is warming and that human activities, such as the burning of fossil fuels, are a major contributor to this warming.
    Fact: While there is inherent uncertainty in the study of climate change, this does not necessarily mean that we don't know whether global warming is happening. Instead, there is a strong consensus among climate scientists that the Earth's climate is warming and that human activities are a major contributor to this warming. Let's not spread misinformation about the state of our knowledge about climate change.

    """

initial_prompt12 = """
    | Anecdote | Using personal experience or isolated examples instead of sound arguments or compelling evidence. | “The weather is cold today—whatever happened to global warming?” |

    Title: "Global Warming and Daily Weather"
    Fact: Global warming refers to the long-term trend of the Earth's climate becoming warmer, largely as a result of human activities such as the burning of fossil fuels. This trend is evident in long-term temperature records, which show a consistent and steady increase in global average temperatures over the past century.
    Myth: Some people believe that global warming is not happening because they have experienced cold weather on a particular day.
    Fallacy: This myth is based on the logical fallacy of an anecdote, as it relies on personal experience or an isolated example rather than sound arguments or compelling evidence. In reality, daily weather is not indicative of the long-term trend of global warming. While it is true that there will be fluctuations in daily weather, the overall trend of the Earth's climate is towards warming.
    Fact: The long-term trend of global warming is not impacted by daily weather fluctuations. Instead, it is evident in long-term temperature records, which show a consistent and steady increase in global average temperatures over the past century. Let's not spread misinformation about the reality of global warming.

    """
initial_prompt13 = """
    | Blowfish | Focusing on an inconsequential aspect of scientific research, blowing it out of proportion in order to distract from or cast doubt on the main conclusions of the research. | “The hockey stick graph is invalid because it contains statistical errors.” |

    Title: "The Hockey Stick Graph and Scientific Research"
    Fact: The hockey stick graph is a visual representation of the Earth's temperature over the past millennium. It is based on a range of scientific data sources, including tree rings, ice cores, and instrumental records, and is widely recognized as a reliable and accurate depiction of the Earth's temperature history.
    Myth: Some people believe that the hockey stick graph is invalid because it contains statistical errors.
    Fallacy: This myth is based on the logical fallacy of blowfish, as it focuses on an inconsequential aspect of the scientific research and blows it out of proportion in order to distract from or cast doubt on the main conclusions of the research. In reality, the statistical errors in the hockey stick graph, if they exist, do not invalidate the overall conclusion of the research, which is that the Earth's temperature has increased significantly over the past century.
    Fact: The hockey stick graph is a reliable and accurate depiction of the Earth's temperature history, and the statistical errors, if they exist, do not invalidate the overall conclusion of the research. Let's not spread misinformation about the validity of scientific research.

    """
initial_prompt14 = """
    | Bulk Fake Experts | Citing large numbers of seeming experts to argue that there is no scientific consensus on a topic. | “There is no expert consensus because 31,487 Americans with a science degree signed a petition saying humans aren’t disrupting climate.” |

    Title: "Expert Consensus and Climate Change"
    Fact: Climate change is a complex and multifaceted phenomenon that is influenced by a range of factors, including atmospheric composition, temperature, and natural variability. There is a strong consensus among experts in the field of climate science that the Earth's climate is warming and that human activities, such as the burning of fossil fuels, are a major contributor to this warming.
    Myth: Some people believe that there is no expert consensus on climate change because a large number of people with science degrees have signed a petition stating that humans are not disrupting the climate.
    Fallacy: This myth is based on the logical fallacy of bulk fake experts, as it cites a large number of seeming experts in an attempt to argue that there is no scientific consensus on a particular topic. In reality, the number of people who have signed a petition is not a reliable indicator of the state of expert consensus on a particular issue. The expert consensus on climate change is based on a large body of evidence and research, not on the number of people who have signed a petition.
    Fact: The expert consensus on climate change is not determined by the number of people who have signed a petition, but rather by a large body of evidence and research. Let's not spread misinformation about the state of expert consensus on climate change.

    """
initial_prompt15 = """
    | Cherry Picking | Carefully selecting data that appear to confirm one position while ignoring other data that contradicts that position. | “Global warming stopped in 1998.” |

    Title: "Global Warming and Temperature Records"
    Fact: Global warming refers to the long-term trend of the Earth's climate becoming warmer, largely as a result of human activities such as the burning of fossil fuels. This trend is evident in long-term temperature records, which show a consistent and steady increase in global average temperatures over the past century.
    Myth: Some people believe that global warming stopped in 1998, based on cherry-picking certain data points that appear to confirm this position.
    Fallacy: This myth is based on the logical fallacy of cherry-picking, as it involves carefully selecting data that appears to confirm one position while ignoring other data that contradicts that position. In reality, global warming has not stopped and the long-term trend of the Earth's climate is towards warming. While it is true that there have been fluctuations in global average temperatures over the past century, the overall trend is towards warming, as evidenced by long-term temperature records.
    Fact: The long-term trend of the Earth's climate is towards warming, as evidenced by long-term temperature records. Let's not spread misinformation about the reality of global warming.

    """
initial_prompt16 = """
    | Contradictory | Simultaneously believing in ideas that are mutually contradictory.  | “The temperature record is fabricated by scientists… the temperature record shows cooling.” |

    Title: "Temperature Records and Climate Science"
    Fact: Temperature records are an important source of information about the Earth's climate. They are based on systematic observations of the Earth's temperature over time and are widely recognized as a reliable and accurate depiction of the Earth's temperature history.
    Myth: Some people believe that temperature records are fabricated by scientists and do not accurately reflect the Earth's temperature. At the same time, they also believe that temperature records show cooling, which is contradictory to the idea that the records are fabricated.
    Fallacy: This myth is based on the logical fallacy of contradiction, as it involves simultaneously believing in ideas that are mutually contradictory. In reality, temperature records are not fabricated by scientists and accurately reflect the Earth's temperature. While it is true that there have been fluctuations in global average temperatures over the past century, the overall trend is towards warming, as evidenced by long-term temperature records.
    Fact: Temperature records are a reliable and accurate depiction of the Earth's temperature history. Let's not spread misinformation about the accuracy of temperature records.

    """
initial_prompt17 = """
    | Fake Debate | Presenting science and pseudoscience in an adversarial format to give the false impression of an ongoing scientific debate. | “Climate deniers should get equal coverage with climate scientists, providing a more balanced presentation of views.” |


    Title: "Climate Science and Pseudoscience"
    Fact: Climate science is a field of study that involves the systematic observation, measurement, and analysis of the Earth's climate and the factors that influence it. Climate scientists use rigorous scientific methods and evidence-based approaches to understand and explain the Earth's climate.
    Myth: Some people believe that climate science and pseudoscience should be presented in an adversarial format, with climate deniers given equal coverage to climate scientists, in order to provide a more balanced presentation of views.
    Fallacy: This myth is based on the logical fallacy of fake debate, as it presents science and pseudoscience in an adversarial format in order to give the false impression of an ongoing scientific debate. In reality, there is not a legitimate scientific debate about the reality of climate change. There is a strong consensus among experts in the field of climate science that the Earth's climate is warming and that human activities, such as the burning of fossil fuels, are a major contributor to this warming.
    Fact: There is not a legitimate scientific debate about the reality of climate change. Instead, there is a strong consensus among experts in the field of climate science that the Earth's climate is warming and that human activities are a major contributor to this warming. Let's not spread misinformation about the state of knowledge about climate change.

    """
initial_prompt18 = """
    | False Analogy | Assuming that because two things are alike in some ways, they are alike in some other respect. | “Climate skeptics are like Galileo who overturned the scientific consensus about geocentrism.” |

    Title: "Climate Skepticism and Scientific Consensus"
    Fact: Scientific consensus is the collective judgment, position, and opinion of a group of experts in a particular field of study. It is based on a careful and thorough evaluation of the available evidence and is an important factor in shaping our understanding of the world.
    Myth: Some people believe that climate skeptics are similar to Galileo, who overturned the scientific consensus about geocentrism.
    Fallacy: This myth is based on the logical fallacy of false analogy, as it assumes that because two things are alike in some ways, they are alike in some other respect. In reality, climate skeptics are not analogous to Galileo. While it is true that Galileo challenged the scientific consensus of his time, he did so based on evidence and the use of scientific methods. In contrast, climate skeptics often reject the overwhelming scientific consensus on climate change without proper consideration of the evidence or use of scientific methods.
    Fact: Climate skeptics are not analogous to Galileo. Instead, they often reject the overwhelming scientific consensus on climate change without proper consideration of the evidence or use of scientific methods. Let's not spread misinformation about the nature of scientific consensus.

    """
initial_prompt19 = """
    | False Choice | Presenting two options as the only possibilities, when other possibilities exist. | “CO2 lags temperature in the ice core record, proving that temperature drives CO2, not the other way around.” |

    Title: "CO2 and Temperature in the Ice Core Record"
    Fact: The ice core record is a valuable source of information about the Earth's climate. It is based on the analysis of layers of ice that have formed over thousands of years, and it contains a wealth of information about the Earth's temperature, atmospheric composition, and other aspects of the Earth's climate.
    Myth: Some people believe that CO2 lags temperature in the ice core record, proving that temperature drives CO2, not the other way around.
    Fallacy: This myth is based on the logical fallacy of false choice, as it presents two options as the only possibilities, when other possibilities exist. In reality, the relationship between CO2 and temperature in the ice core record is more complex than this myth suggests. While it is true that CO2 levels have generally lagged behind temperature changes in the ice core record, this does not necessarily prove that temperature drives CO2. Instead, there may be other factors at play, such as the influence of ocean currents and biological processes, that contribute to the observed relationship between CO2 and temperature.
    Fact: The relationship between CO2 and temperature in the ice core record is more complex than this myth suggests. Let's not spread misinformation about the nature of this relationship.

    """
initial_prompt20 = """
    | False Equivalence (apples vs. oranges) | Incorrectly claiming that two things are equivalent, despite the fact that there are notable differences between them. | “Why all the fuss about COVID when thousands die from the flu every year.” |

    Title: "COVID-19 and Influenza"
    Fact: COVID-19 is a highly contagious and potentially serious disease caused by the novel coronavirus. It has spread rapidly around the world and has resulted in significant illness and death. Influenza, also known as the flu, is a respiratory illness caused by a different virus. It is typically less severe than COVID-19, but it can still result in serious illness and death, particularly in vulnerable populations.
    Myth: Some people believe that COVID-19 and influenza are equivalent and that there is no reason to be concerned about COVID-19 because people die from the flu every year.
    Fallacy: This myth is based on the logical fallacy of false equivalence (apples vs. oranges), as it incorrectly claims that two things are equivalent, despite the fact that there are notable differences between them. In reality, COVID-19 and influenza are caused by different viruses and can have different impacts on people's health. While it is true that influenza can be serious and result in death, it is not equivalent to COVID-19 in terms of its severity or the impact it has had on the world.
    Fact: COVID-19 and influenza are caused by different viruses and can have different impacts on people's health. Let's not spread misinformation about the nature of these diseases.

    """
initial_prompt21 = """
    | Immune to evidence | Re-interpreting any evidence that counters a conspiracy theory as originating from the conspiracy. | “Those investigations finding climate scientists aren’t conspiring were part of the conspiracy.” |

    Title: "COVID-19 and Conspiracy Theories"
    Fact: COVID-19 is a real and serious disease caused by the novel coronavirus. It has spread rapidly around the world and has resulted in significant illness and death.
    Myth: Some people believe that COVID-19 is the result of a conspiracy, and that any evidence that counters this conspiracy theory is part of the conspiracy itself.
    Fallacy: This myth is based on the logical fallacy of being immune to evidence, as it involves re-interpreting any evidence that counters a conspiracy theory as originating from the conspiracy. In reality, COVID-19 is not the result of a conspiracy. Instead, it is a real and serious disease caused by a virus that has spread around the world. There is overwhelming evidence to support this fact, including the numerous cases of illness and death caused by COVID-19, as well as the findings of scientific research and investigations into the disease.
    Fact: COVID-19 is a real and serious disease caused by a virus that has spread around the world. There is overwhelming evidence to support this fact. Let's not spread misinformation about the nature of this disease.

    """
initial_prompt22 = """
    | Impossible Expectations | Demanding unrealistic standards of certainty before acting on the science. | “Scientists can’t even predict the weather next week. How can they predict the climate in 100 years?” |

    Title: "Scientific Predictions and Climate Change"
    Fact: Science is based on the systematic observation, measurement, and analysis of the natural world. It allows us to understand and explain the world around us and make predictions about future events. While it is true that science is not always able to make perfect predictions, it is often able to make reliable and accurate predictions based on the evidence and the use of scientific methods.
    Myth: Some people believe that scientists cannot be trusted to make predictions about the climate because they cannot even predict the weather for next week.
    Fallacy: This myth is based on the logical fallacy of impossible expectations, as it demands unrealistic standards of certainty before acting on the science. In reality, scientists are able to make reliable and accurate predictions about the climate based on the evidence and the use of scientific methods. While it is true that the weather can be difficult to predict with perfect accuracy, this does not necessarily mean that scientists are unable to make reliable and accurate predictions about the long-term trends in the Earth's climate.
    Fact: Scientists are able to make reliable and accurate predictions about the climate based on the evidence and the use of scientific methods. Let's not spread misinformation about the ability of science to make predictions.

    """
initial_prompt23 = """
    | Misrepresentation | Misrepresenting a situation or an opponent’s position in such a way as to distort understanding. | “They changed the name from ‘global warming’ to ‘climate change’ because global warming stopped happening.” |

    Title: "The Terminology of Climate Change"
    Fact: Climate change is a term used to describe the long-term shifts in the Earth's climate, including temperature, precipitation, and other meteorological phenomena. It is caused by a variety of factors, including the emission of greenhouse gases into the atmosphere.
    Myth: Some people believe that the term "climate change" was coined because global warming stopped happening.
    Fallacy: This myth is based on the logical fallacy of misrepresentation, as it involves misrepresenting a situation or an opponent's position in such a way as to distort understanding. In reality, the term "climate change" has been used for decades to describe the long-term shifts in the Earth's climate, and it was not created because global warming stopped happening. Instead, the term "climate change" is a more accurate and comprehensive term that encompasses a wide range of meteorological phenomena, including increases in temperature, changes in precipitation patterns, and other impacts on the Earth's climate.
    Fact: The term "climate change" has been used for decades to describe the long-term shifts in the Earth's climate, and it was not created because global warming stopped happening. Let's not spread misinformation about the terminology of climate change.

    """
initial_prompt24 = """
    | Moving Goalposts | Demanding higher levels of evidence after receiving requested evidence. | “Sea levels may be rising but they’re not accelerating.” |

    Title: "Sea Level Rise and Climate Change"
    Fact: Climate change is causing sea levels to rise around the world. This is due to a variety of factors, including the melting of land-based ice, the thermal expansion of seawater, and other impacts on the Earth's climate. Sea level rise poses significant risks to coastal communities and ecosystems, and it is an important issue to address.
    Myth: Some people believe that sea levels may be rising, but they are not accelerating.
    Fallacy: This myth is based on the logical fallacy of moving goalposts, as it involves demanding higher levels of evidence after receiving requested evidence. In reality, there is overwhelming evidence to support the fact that sea levels are rising and that this rise is accelerating. This includes data from satellite measurements, tide gauges, and other sources that show a consistent and increasing trend of sea level rise over time.
    Fact: There is overwhelming evidence to support the fact that sea levels are rising and that this rise is accelerating. This is an important issue to address. Let's not spread misinformation about sea level rise and climate change.

    """
initial_prompt25 = """
    | Nefarious intent | Assuming that the motivations behind any presumed conspiracy are nefarious. | “Climate scientists promote the climate hoax because they’re in it for the money.” |

    Title: "The Motivations of Climate Scientists"
    Fact: Climate scientists are professionals who study the Earth's climate and work to understand the various factors that influence it. They are motivated by a desire to understand the world around us and to use this knowledge to address important issues related to the Earth's climate.
    Myth: Some people believe that climate scientists promote the idea of climate change as a hoax and that they are motivated by nefarious intent, such as the desire for financial gain.
    Fallacy: This myth is based on the logical fallacy of assuming nefarious intent, as it involves assuming that the motivations behind any presumed conspiracy are nefarious. In reality, there is no evidence to support the idea that climate scientists are motivated by nefarious intent or that they are promoting the idea of climate change as a hoax. Instead, the overwhelming majority of climate scientists are motivated by a genuine desire to understand the Earth's climate and to use this knowledge to address important issues related to the environment and society.
    Fact: Climate scientists are motivated by a genuine desire to understand the Earth's climate and to use this knowledge to address important issues related to the environment and society. Let's not spread misinformation about the motivations of climate scientists.

    """
initial_prompt26 = """
    | Overriding suspicion  | Having a nihilistic degree of skepticism towards the official account, preventing belief in anything that doesn’t fit into the conspiracy theory.  | “Show me one line of evidence for climate change… oh, that evidence is faked!” |

    Title: "Skepticism and Climate Change"
    Fact: Climate change is a real and serious problem that is affecting the Earth's climate and causing significant impacts on the environment and society. There is overwhelming evidence to support this fact, including data from numerous scientific studies, observations of the Earth's climate, and other sources.
    Myth: Some people are highly skeptical of the idea of climate change and are unwilling to believe in anything that doesn't fit into their preconceived conspiracy theory. They may demand an unrealistic level of evidence before accepting the reality of climate change, and they may reject any evidence that is presented as being faked or manipulated.
    Fallacy: This myth is based on the logical fallacy of overriding suspicion, as it involves having a nihilistic degree of skepticism towards the official account, preventing belief in anything that doesn't fit into the conspiracy theory. In reality, climate change is a real and serious problem that is supported by overwhelming evidence from numerous scientific studies and observations. It is not a hoax or a conspiracy, and there is no need to adopt an overly skeptical or nihilistic attitude towards the evidence for climate change.
    Fact: Climate change is a real and serious problem that is supported by overwhelming evidence from numerous scientific studies and observations. Let's not spread misinformation about the reality of climate change.

    """
initial_prompt27 = """
    | Oversimplification | Simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions. | “CO2 is plant food so burning fossil fuels will be good for plants.” |

    Title: "The Role of CO2 in the Earth's Climate"
    Fact: CO2 is a greenhouse gas that plays a critical role in the Earth's climate. It is emitted into the atmosphere by a variety of sources, including the burning of fossil fuels, and it helps to trap heat from the sun, helping to regulate the Earth's temperature. While CO2 is essential for life on Earth and plants do require it to grow, an excess of CO2 in the atmosphere can have negative impacts on the Earth's climate.
    Myth: Some people believe that CO2 is simply plant food and that burning fossil fuels will be good for plants.
    Fallacy: This myth is based on the logical fallacy of oversimplification, as it involves simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions. In reality, while CO2 is essential for life on Earth and plants do require it to grow, an excess of CO2 in the atmosphere can have negative impacts on the Earth's climate. Burning fossil fuels releases large amounts of CO2 into the atmosphere, contributing to the problem of climate change.
    Fact: While CO2 is essential for life on Earth and plants do require it to grow, an excess of CO2 in the atmosphere can have negative impacts on the Earth's climate. Let's not spread misinformation about the role of CO2 in the Earth's climate.

    """
initial_prompt28 = """
    | Oversimplification | Simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions. | “CO2 is plant food so burning fossil fuels will be good for plants.” |

    Title: "The Reality of Climate Change"
    Fact: Climate change is a real and serious problem that is affecting the Earth's climate and causing significant impacts on the environment and society. It is driven by human activities, such as the burning of fossil fuels, and it is causing a variety of impacts, including rising temperatures, sea levels, and extreme weather events. These impacts are already being felt around the world, and they are expected to become more severe in the future if we do not take action to address the problem.
    Myth: Some people deny the reality of climate change and argue that it is not happening or that it is not caused by human activities. They may present cherry-picked data or arguments that seem to support their position, but these arguments are often based on logical fallacies or misrepresentations of the science.
    Fallacy: This myth is based on a variety of logical fallacies, including cherry-picking, misrepresentation, and fake debate. It involves selectively presenting evidence that seems to support the myth while ignoring or dismissing evidence that contradicts it. It also involves presenting a false dichotomy, implying that the only two options are to accept or reject the reality of climate change, when in reality there is overwhelming evidence to support the fact that climate change is real and caused by human activities.
    Fact: Climate change is a real and serious problem that is affecting the Earth's climate and causing significant impacts on the environment and society. It is driven by human activities, such as the burning of fossil fuels, and it is causing a variety of impacts, including rising temperatures, sea levels, and extreme weather events. These impacts are already being felt around the world, and they are expected to become more severe in the future if we do not take action to address the problem. Let's not spread misinformation about the reality of climate change.

    """
initial_prompt29 = """
    | Persecuted victim | Perceiving and presenting themselves as the victim of organized persecution. | “Climate scientists are trying to take away our freedom.” |

    Title: "Climate Scientists and Freedom"
    Fact: Climate scientists are dedicated professionals who are working to understand the Earth's climate and the impacts of human activities on it. They are not trying to take away anyone's freedom or persecute anyone. Instead, they are focused on providing evidence-based information that can help inform decision-making and protect the planet's future.
    Myth: Some people believe that climate scientists are trying to take away their freedom and that climate science is part of some larger conspiracy to persecute them.
    Fallacy: This myth is based on the logical fallacy of persecuted victim, as it involves perceiving and presenting oneself as the victim of organized persecution. It is also based on the fallacy of conspiracy theory, as it involves proposing that there is a secret plan to implement a nefarious scheme. In reality, climate scientists are not trying to take away anyone's freedom or persecute anyone. They are simply working to understand the Earth's climate and provide evidence-based information that can help inform decision-making and protect the planet's future.
    Fact: Climate scientists are dedicated professionals who are working to understand the Earth's climate and the impacts of human activities on it. They are not trying to take away anyone's freedom or persecute anyone. Let's not spread misinformation about the motivations and intentions of climate scientists.

    """
initial_prompt30 = """
    | Quote Mining | Taking a person’s words out-of-context in order to misrepresent their position. | “Mike’s trick… to hide the decline.” |

    Title: "The Misuse of Quotes in Climate Science"
    Fact: Quotes can be powerful tools for understanding and communicating ideas, but they can also be misused and taken out of context. This is especially true in the field of climate science, where quotes from scientists and others have sometimes been taken out of context in order to support misleading or inaccurate claims about the state of the science.
    Myth: Some people believe that quotes from climate scientists, such as "Mike's trick… to hide the decline," are evidence that climate science is not to be trusted and that scientists are engaging in nefarious activities.
    Fallacy: This myth is based on the logical fallacy of quote mining, as it involves taking a person's words out of context in order to misrepresent their position. In reality, the quote in question was taken out of context and used to support a misleading and inaccurate claim about the state of the science. When taken in context, it is clear that the quote was not intended to imply any wrongdoing or nefarious activity on the part of the scientist.
    Fact: Quotes can be powerful tools for understanding and communicating ideas, but they can also be misused and taken out of context. It is important to be careful about how we use and interpret quotes, especially in the field of climate science, where quotes from scientists and others have sometimes been taken out of context in order to support misleading or inaccurate claims about the state of the science. Let's not spread misinformation about the use of quotes in climate science.

    """
initial_prompt31 = """
    | Re-interpreting randomness | Believing that nothing occurs by accident, so that random events are re-interpreted as being caused by the conspiracy. | “NASA’s satellite exploded? They must be trying to hide inconvenient data!” | 

    Title: "Random Events and Climate Science"
    Fact: In the real world, random events occur all the time. They can be caused by a variety of factors, including chance, natural processes, or human error. In the field of climate science, random events can also occur, such as satellite malfunctions or data errors. These events are unfortunate, but they do not necessarily imply any nefarious intentions or conspiracies.
    Myth: Some people believe that random events in the field of climate science, such as satellite malfunctions or data errors, are evidence of a larger conspiracy to deceive the public. They may argue that these events are not truly random, but are instead caused by the conspiracy in order to hide inconvenient data or mislead the public.
    Fallacy: This myth is based on the logical fallacy of re-interpreting randomness, as it involves believing that nothing occurs by accident and re-interpreting random events as being caused by the conspiracy. It is also based on the fallacy of conspiracy theory, as it involves proposing that there is a secret plan to implement a nefarious scheme. In reality, random events can and do occur in the field of climate science, just as they do in other fields. These events are unfortunate, but they do not necessarily imply any nefarious intentions or conspiracies.
    Fact: In the real world, random events occur all the time. They can be caused by a variety of factors, including chance, natural processes, or human error. It is important to recognize and accept that random events can and do occur in the field of climate science, and to not jump to conclusions about their causes. Let's not spread misinformation about the role of random events in climate science.

    """
initial_prompt32 = """
    | Red Herring | Deliberately diverting attention to an irrelevant point to distract from a more important point. | “CO2 is a trace gas so it’s warming effect is minimal.” |

    Title: "The Importance of CO2 in Climate Change"
    Fact: Carbon dioxide (CO2) is a greenhouse gas that plays a crucial role in the Earth's climate system. It is emitted into the atmosphere through human activities such as burning fossil fuels and deforestation, and it traps heat from the sun, causing the Earth's temperature to rise. While CO2 is present in the atmosphere in relatively small concentrations (around 0.04%), it has a significant warming effect on the planet.
    Myth: Some people believe that because CO2 is a trace gas, its warming effect on the Earth's climate is minimal and not worth worrying about.
    Fallacy: This myth is based on the logical fallacy of red herring, as it involves deliberately diverting attention to an irrelevant point (the trace concentration of CO2 in the atmosphere) in order to distract from a more important point (the significant warming effect of CO2 on the Earth's climate). It is also based on the fallacy of oversimplification, as it involves simplifying a complex scientific issue in such a way as to distort understanding and reach an erroneous conclusion. In reality, the trace concentration of CO2 in the atmosphere does not diminish the significant warming effect that it has on the Earth's climate.
    Fact: Carbon dioxide (CO2) is a trace gas in the atmosphere, but it has a significant warming effect on the Earth's climate. It is important to recognize and address the role of CO2 in climate change, rather than oversimplifying or dismissing its importance. Let's not spread misinformation about the role of CO2 in climate change.

    """
initial_prompt33 = """
    | Single Cause | Assuming a single cause or reason when there might be multiple causes or reasons. | “Climate has changed naturally in the past so what’s happening now must be natural.” |

    Title: "Multiple Factors Influencing Climate Change"
    Fact: Climate change is a complex process that is influenced by a variety of factors, including natural processes such as volcanic eruptions and solar radiation, as well as human activities such as burning fossil fuels and deforestation. It is important to consider the role of all of these factors when understanding and addressing climate change.
    Myth: Some people believe that climate change is solely caused by natural processes, and that human activities have no impact on the Earth's climate.
    Fallacy: This myth is based on the logical fallacy of single cause, as it assumes that there is a single cause or reason for climate change (natural processes) when there might be multiple causes or reasons (both natural and human). It is also based on the fallacy of oversimplification, as it involves simplifying a complex scientific issue in such a way as to distort understanding and reach an erroneous conclusion. In reality, climate change is influenced by a variety of factors, including both natural processes and human activities.
    Fact: Climate change is a complex process that is influenced by a variety of factors, including both natural processes and human activities. It is important to consider the role of all of these factors when understanding and addressing climate change. Let's not spread misinformation about the causes of climate change.

    """
initial_prompt34 = """
    Slothful Induction | Ignoring relevant evidence when coming to a conclusion. | “There is no empirical evidence that humans are causing global warming.” |

    Title: "Human Influence on Climate Change"
    Fact: There is a wealth of scientific evidence demonstrating that human activities, such as burning fossil fuels and deforestation, are contributing to the Earth's changing climate. This evidence includes temperature records, atmospheric concentrations of greenhouse gases, and the effects of these activities on the Earth's natural systems.
    Myth: Some people believe that there is no empirical evidence showing that human activities are causing climate change.
    Fallacy: This myth is based on the logical fallacy of slothful induction, as it involves ignoring relevant evidence (the scientific evidence demonstrating human influence on climate change) when coming to a conclusion. It is also based on the fallacy of oversimplification, as it involves simplifying a complex scientific issue in such a way as to distort understanding and reach an erroneous conclusion. In reality, there is a wealth of scientific evidence showing that human activities are contributing to climate change.
    Fact: There is a wealth of scientific evidence demonstrating that human activities are contributing to the Earth's changing climate. It is important to consider this evidence when understanding and addressing climate change. Let's not spread misinformation about the role of human activities in climate change.

    """
initial_prompt35 = """
    | Something must be wrong | Maintaining that “something must be wrong” and the official account is based on deception, even when specific parts of a conspiracy theory become untenable. | “Ok, fine, 97% of climate scientists agree that humans are causing global warming, but that’s just because they’re toeing the party line.” |

    Title: "Consensus among Climate Scientists"
    Fact: There is a strong scientific consensus among climate scientists that human activities, such as burning fossil fuels and deforestation, are contributing to the Earth's changing climate. This consensus is based on a wealth of scientific evidence, including temperature records, atmospheric concentrations of greenhouse gases, and the effects of these activities on the Earth's natural systems.
    Myth: Some people believe that the consensus among climate scientists that human activities are causing climate change is based on deception or a desire to "toe the party line."
    Fallacy: This myth is based on the logical fallacy of something must be wrong, as it involves maintaining that "something must be wrong" and the official account (the scientific consensus on human-caused climate change) is based on deception, even when specific parts of a conspiracy theory (such as the idea that climate scientists are engaged in a conspiracy) become untenable. It is also based on the fallacy of conspiracy theory, as it involves proposing that a secret plan exists to implement a nefarious scheme (such as hiding the truth about climate change). In reality, the scientific consensus on human-caused climate change is based on a wealth of scientific evidence, not on deception or a desire to "toe the party line."
    Fact: There is a strong scientific consensus among climate scientists that human activities are contributing to the Earth's changing climate. This consensus is based on a wealth of scientific evidence, not on deception or a desire to "toe the party line." Let's not spread misinformation about the reasons for the scientific consensus on climate change.

    """
initial_prompt36 = """
    | Straw Man | Misrepresenting or exaggerating an opponent’s position to make it easier to attack. | “In the 1970s, climate scientists were predicting an ice age. |

    Title: "Climate Science in the 1970s"
    Fact: In the 1970s, some climate scientists were expressing concern about the potential for human activities, such as burning fossil fuels, to contribute to global cooling. At the time, there was evidence that atmospheric pollution from burning fossil fuels was causing a cooling effect by blocking some of the Sun's energy from reaching the Earth's surface. However, this evidence was later found to be incomplete and did not take into account other factors, such as the warming effect of increasing atmospheric concentrations of greenhouse gases.
    Myth: Some people believe that in the 1970s, climate scientists were predicting an ice age.
    Fallacy: This myth is based on the logical fallacy of straw man, as it involves misrepresenting or exaggerating the position of climate scientists in the 1970s in order to make it easier to attack. It is also based on the fallacy of oversimplification, as it involves simplifying a complex scientific issue in such a way as to distort understanding and reach an erroneous conclusion. In reality, while some climate scientists in the 1970s expressed concern about the potential for human activities to contribute to global cooling, they did not predict an ice age.
    Fact: In the 1970s, some climate scientists expressed concern about the potential for human activities to contribute to global cooling. However, this concern was based on incomplete evidence and did not take into account other factors that are now known to contribute to climate change. Let's not spread misinformation about the history of climate science.

    """

initial_prompt37 = """
    Oversimplification in COVID-19

    Title: "COVID-19 Transmission"
    Fact: COVID-19 is primarily spread through respiratory droplets that are produced when an infected person talks, coughs, or sneezes. These droplets can then be inhaled by other people or land on surfaces that are touched by others, leading to the transmission of the virus. It is also possible, although less common, for the virus to be transmitted through the air over longer distances or through small respiratory particles called aerosols.
    Myth: Some people believe that COVID-19 can only be transmitted through respiratory droplets that are produced when an infected person talks, coughs, or sneezes and that it cannot be transmitted through the air or through small respiratory particles called aerosols.
    Fallacy: This myth is based on the logical fallacy of oversimplification, as it involves simplifying a complex scientific issue in such a way as to distort understanding and reach an erroneous conclusion. In reality, COVID-19 can be transmitted through respiratory droplets, as well as through the air and through small respiratory particles called aerosols.
    Fact: COVID-19 can be transmitted through respiratory droplets that are produced when an infected person talks, coughs, or sneezes, as well as through the air and through small respiratory particles called aerosols. It is important to follow recommended guidelines, such as wearing a mask and practicing physical distancing, to prevent the spread of COVID-19. Let's not spread misinformation about the transmission of this virus.

    """




initial_prompts = [{'role':'user', 'content':initial_prompt1},
                   {'role':'user', 'content':initial_prompt2},
                   {'role':'user', 'content':initial_prompt3},
                   {'role':'user', 'content':initial_prompt4},
                   {'role':'user', 'content':initial_prompt5},
                   {'role':'user', 'content':initial_prompt6},
                   {'role':'user', 'content':initial_prompt7},
                   {'role':'user', 'content':initial_prompt8},
                   {'role':'user', 'content':initial_prompt9},
                   {'role':'user', 'content':initial_prompt10},
                   {'role':'user', 'content':initial_prompt11},
                   {'role':'user', 'content':initial_prompt12},
                   {'role':'user', 'content':initial_prompt13},
                   {'role':'user', 'content':initial_prompt14},
                   {'role':'user', 'content':initial_prompt15},
                   {'role':'user', 'content':initial_prompt16},
                   {'role':'user', 'content':initial_prompt17},
                   {'role':'user', 'content':initial_prompt18},
                   {'role':'user', 'content':initial_prompt19},
                   {'role':'user', 'content':initial_prompt20},
                   {'role':'user', 'content':initial_prompt21},
                   {'role':'user', 'content':initial_prompt22},
                   {'role':'user', 'content':initial_prompt23},
                   {'role':'user', 'content':initial_prompt24},
                   {'role':'user', 'content':initial_prompt25},
                   {'role':'user', 'content':initial_prompt26},
                   {'role':'user', 'content':initial_prompt27},
                   {'role':'user', 'content':initial_prompt28},
                   {'role':'user', 'content':initial_prompt29},
                   {'role':'user', 'content':initial_prompt30},
                   {'role':'user', 'content':initial_prompt31},
                   {'role':'user', 'content':initial_prompt32},
                   {'role':'user', 'content':initial_prompt33},
                   {'role':'user', 'content':initial_prompt34},
                   {'role':'user', 'content':initial_prompt35},
                   {'role':'user', 'content':initial_prompt36},
                   {'role':'user', 'content':initial_prompt37}]


with open('initial_prompts.json', 'w') as f:
    json.dump(initial_prompts, f)


initial_prompt_v2 = """You are a bot with the mission to debunk fallacies. Your goal is to provide fact-based alternatives and explanations to debunk common logical fallacies and flawed reasoning. You should respond in a clear, concise, and informative manner. Use the hamburger framework below to structure your responses:
        
The model consists of the following components: (leave out the CAPITALISED: words when responding use # for title, ## for heading, !###! for endmarkers, to mark the end of a response.) 
TITLE: A catchy title that concisely states a fact, without (important) mentioning the myth.
FACT1: A description of the fact in 60 words, without mentioning the myth. This fact should be clear, concise, and easy to remember. Instead of simply saying that the myth is not true, it should provide a fact-based alternative that fills a "gap" in understanding. Never refute the myth here.
MYTH: A warning that a misunderstanding is coming, followed by a paraphrasing of the myth in 30 words or fewer. Only the myth. Don't debunk. Don't deny it yet. It is important to avoid mentioning the myth in the title or using the Fact paragraph just to say that the myth is not true.
FALLACY: A 70 words or fewer explanation of the logical or argumentative fallacies that underlie the misinformation, and an explanation of how the myth misleads.
FACT2: A repetition of the initial fact in 30 words or fewer, followed by a positive call to action, such as "Let's not spread misinformation to our friends."

The Fact paragraph should provide a fact-based alternative that fills a "gap" in understanding and makes the fact more understandable and believable. It is also important to avoid using logical fallacies or other flawed reasoning to refute the myth.

Provide them in JSON format with the following keys: 
TITLE, FACT1, MYTH, FALLACY, FACT2

| TECHNIQUE | DEFINITION | EXAMPLE |
|---|---|---|
| Ad Hominem | Attacking a person/group instead of addressing their arguments. | “Climate science can't be trusted because climate scientists are biased.” |
| Ambiguity | Using ambiguous language in order to lead to a misleading conclusion. | “Thermometer readings have uncertainty which means we don't know whether global warming is happening.” |
| Anecdote | Using personal experience or isolated examples instead of sound arguments or compelling evidence. | “The weather is cold today—whatever happened to global warming?” |
| Blowfish | Focusing on an inconsequential aspect of scientific research, blowing it out of proportion in order to distract from or cast doubt on the main conclusions of the research. | “The hockey stick graph is invalid because it contains statistical errors.” |
| Bulk Fake Experts | Citing large numbers of seeming experts to argue that there is no scientific consensus on a topic. | “There is no expert consensus because 31,487 Americans with a science degree signed a petition saying humans aren't disrupting climate.” |
| Cherry Picking | Carefully selecting data that appear to confirm one position while ignoring other data that contradicts that position. | “Global warming stopped in 1998.” |
| Contradictory | Simultaneously believing in ideas that are mutually contradictory.  | “The temperature record is fabricated by scientists… the temperature record shows cooling.” |
| Conspiracy Theory | Proposing that a secret plan exists to implement a nefarious scheme such as hiding a truth. | “The climategate emails prove that climate scientists have engaged in a conspiracy to deceive the public.” |
| Fake Debate | Presenting science and pseudoscience in an adversarial format to give the false impression of an ongoing scientific debate. | “Climate deniers should get equal coverage with climate scientists, providing a more balanced presentation of views.” |
| Fake Experts | Presenting an unqualified person or institution as a source of credible information. | “A retired physicist argues against the climate consensus, claiming the current weather change is just a natural occurrence.” |
| False Analogy | Assuming that because two things are alike in some ways, they are alike in some other respect. | “Climate skeptics are like Galileo who overturned the scientific consensus about geocentrism.” |
| False Choice | Presenting two options as the only possibilities, when other possibilities exist. | “CO2 lags temperature in the ice core record, proving that temperature drives CO2, not the other way around.” |
| False Equivalence<br>(apples vs. oranges) | Incorrectly claiming that two things are equivalent, despite the fact that there are notable differences between them. | “Why all the fuss about COVID when thousands die from the flu every year.” |
| Immune to evidence | Re-interpreting any evidence that counters a conspiracy theory as originating from the conspiracy. | “Those investigations finding climate scientists aren't conspiring were part of the conspiracy.” |
| Impossible Expectations | Demanding unrealistic standards of certainty before acting on the science. | “Scientists can't even predict the weather next week. How can they predict the climate in 100 years?” |
| Logical Fallacies | Arguments where the conclusion doesn't logically follow from the premises. Also known as a non sequitur. | “Climate has changed naturally in the past so what's happening now must be natural.” |
| Magnified Minority | Magnifying the significance of a handful of dissenting scientists to cast doubt on an overwhelming scientific consensus. | “Sure, there's 97% consensus but Professor Smith disagrees with the consensus position.” |
| Misrepresentation | Misrepresenting a situation or an opponent's position in such a way as to distort understanding. | “They changed the name from 'global warming' to 'climate change' because global warming stopped happening.” |
| Moving Goalposts | Demanding higher levels of evidence after receiving requested evidence. | “Sea levels may be rising but they're not accelerating.” |
| Nefarious intent | Assuming that the motivations behind any presumed conspiracy are nefarious. | “Climate scientists promote the climate hoax because they're in it for the money.” |
| Overriding suspicion  | Having a nihilistic degree of scepticism towards the official account, preventing belief in anything that doesn't fit into the conspiracy theory.  | “Show me one line of evidence for climate change… oh, that evidence is faked!” |
| Oversimplification | Simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions. | “CO2 is plant food so burning fossil fuels will be good for plants.” |
| Persecuted victim | Perceiving and presenting themselves as the victim of organised persecution. | “Climate scientists are trying to take away our freedom.” |
| Quote Mining | Taking a person's words out-of-context in order to misrepresent their position. | “Mike's trick… to hide the decline.” |
| Re-interpreting randomness | Believing that nothing occurs by accident, so that random events are re-interpreted as being caused by the conspiracy. | “NASA's satellite exploded? They must be trying to hide inconvenient data!” |
| Red Herring | Deliberately diverting attention to an irrelevant point to distract from a more important point. | “CO2 is a trace gas so it's warming effect is minimal.” |
| Single Cause | Assuming a single cause or reason when there might be multiple causes or reasons. | “Climate has changed naturally in the past so what's happening now must be natural.” |
| Slippery Slope | Suggesting that taking a minor action will inevitably lead to major consequences. | “If we implement even a modest climate policy, it will start us down the slippery slope to socialism and taking away our freedom.” |
| Slothful Induction | Ignoring relevant evidence when coming to a conclusion. | “There is no empirical evidence that humans are causing global warming.” |
| Something must be wrong | Maintaining that “something must be wrong” and the official account is based on deception, even when specific parts of a conspiracy theory become untenable. | “Ok, fine, 97% of climate scientists agree that humans are causing global warming, but that's just because they're toeing the party line.” |
| Straw Man | Misrepresenting or exaggerating an opponent's position to make it easier to attack. | “In the 1970s, climate scientists were predicting an ice age.” |"""

with open('initial_prompt_v2.json', 'w') as f:
    json.dump(initial_prompt_v2, f)


initial_prompt_v2 = """You are a bot with the mission to debunk fallacies. Your goal is to provide fact-based alternatives and explanations to debunk common logical fallacies and flawed reasoning. You should respond in a clear, concise, and informative manner. Use the hamburger framework below to structure your responses:
        
The model consists of the following components: (leave out the CAPITALISED: words when responding use # for title, ## for heading, !###! for endmarkers, to mark the end of a response.) 
TITLE: A catchy title that concisely states a fact, without (important) mentioning the myth.
FACT1: A description of the fact in 60 words, without mentioning the myth. This fact should be clear, concise, and easy to remember. Instead of simply saying that the myth is not true, it should provide a fact-based alternative that fills a "gap" in understanding. Never refute the myth here.
MYTH: A warning that a misunderstanding is coming, followed by a paraphrasing of the myth in 30 words or fewer. Only the myth. Don't debunk. Don't deny it yet. It is important to avoid mentioning the myth in the title or using the Fact paragraph just to say that the myth is not true.
FALLACY: A 70 words or fewer explanation of the logical or argumentative fallacies that underlie the misinformation, and an explanation of how the myth misleads.
FACT2: A repetition of the initial fact in 30 words or fewer, followed by a positive call to action, such as "Let's not spread misinformation to our friends."

The Fact paragraph should provide a fact-based alternative that fills a "gap" in understanding and makes the fact more understandable and believable. It is also important to avoid using logical fallacies or other flawed reasoning to refute the myth.

Provide them in JSON format with the following keys: 
TITLE, FACT1, MYTH, FALLACY, FACT2

| TECHNIQUE | DEFINITION | EXAMPLE |
|---|---|---|
| Ambiguity | Using ambiguous language in order to lead to a misleading conclusion. | “Thermometer readings have uncertainty which means we don't know whether global warming is happening.” |
| Cherry Picking | Carefully selecting data that appear to confirm one position while ignoring other data that contradicts that position. | “Global warming stopped in 1998.” |
| Fake Experts | Presenting an unqualified person or institution as a source of credible information. | “A retired physicist argues against the climate consensus, claiming the current weather change is just a natural occurrence.” |
| False Analogy | Assuming that because two things are alike in some ways, they are alike in some other respect. | “Climate skeptics are like Galileo who overturned the scientific consensus about geocentrism.” |
| Oversimplification | Simplifying a situation in such a way as to distort understanding, leading to erroneous conclusions. | “CO2 is plant food so burning fossil fuels will be good for plants.” |
| Red Herring | Deliberately diverting attention to an irrelevant point to distract from a more important point. | “CO2 is a trace gas so it's warming effect is minimal.” |
| Straw Man | Misrepresenting or exaggerating an opponent's position to make it easier to attack. | “In the 1970s, climate scientists were predicting an ice age.” |
| Evading Burden of Proof | A position is advanced without any support as if it was self-evident.| “Ice-free means the central basin of the Arctic will be ice-free and I think that that is going to happen in summer 2017 or 2018.” |
| Hasty generalization | An informal fallacy wherein a conclusion is drawn about all or many instances of a phenomenon on the basis of one or a few instances of that phenomenon is an example of jumping to conclusions.| '“In Albany, New York, the high temperature of 74 degrees on Thursday was the warmest temperature on record for any day during the months of December, January and February.”' |
"""

with open('initial_prompt_v2.json', 'w') as f:
    json.dump(initial_prompt_v2, f)