CREATE VIEW tempo2
AS 
SELECT
c.claims_id,
tp.premise AS true_premise,
tp.premise_identifier AS true_premise_identifier,
tf.fallacy_text AS true_fallacy,
tp.is_hidden as tp_hidden
FROM Claims c
inner JOIN True_Premises tp
ON c.claims_id = tp.claims_id
inner JOIN True_Fallacies tf
ON tp.premise_id = tf.premise_id
WHERE tp.premise_identifier != 'C'
