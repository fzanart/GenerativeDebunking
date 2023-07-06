CREATE VIEW tempo 
AS 
SELECT
c.claims_id,
pp.premise AS pred_premise,
pp.premise_identifier AS pred_premise_identifier,
pf.fallacy_text AS pred_fallacy,
pp.is_hidden as pp_hidden
FROM Claims c
inner JOIN Pred_Premises pp
ON c.claims_id = pp.claims_id
inner JOIN Pred_Fallacies pf
ON pp.premise_id = pf.premise_id
WHERE pp.premise_identifier != 'C'