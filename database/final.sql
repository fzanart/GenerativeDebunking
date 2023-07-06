select *
from tempo a
inner join tempo2 b
on a.claims_id = b.claims_id
where a.pred_premise_identifier = b.true_premise_identifier and a.pred_fallacy = b.true_fallacy
order by 1