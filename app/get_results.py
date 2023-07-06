import argparse
import sqlite3
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

query = """SELECT *
FROM (
    SELECT
        c.claims_id,
        c.claims_text,
        tp.premise AS true_premise,
        tp.premise_identifier AS true_premise_identifier,
		COALESCE(tf.fallacy_text, 'no fallacy') AS true_fallacy_text,
        pp.premise AS pred_premise,
        pp.premise_identifier AS pred_premise_identifier,
        pf.fallacy_text AS pred_fallacy_text,
		CASE WHEN (LOWER(tf.fallacy_text) = LOWER(pf.fallacy_text)) OR (tf.fallacy_text IS NULL AND pf.fallacy_text = 'no fallacy') THEN 1 ELSE 0 END AS fallacy_match
    FROM
        Claims c
    LEFT JOIN
        True_Premises tp ON c.claims_id = tp.claims_id
    LEFT JOIN
        True_Fallacies tf ON tp.premise_id = tf.premise_id
    LEFT JOIN
        Pred_Premises pp ON c.claims_id = pp.claims_id
    LEFT JOIN
        Pred_Fallacies pf ON pp.premise_id = pf.premise_id
) AS subquery
WHERE
    subquery.true_premise_identifier = subquery.pred_premise_identifier
	AND subquery.true_premise_identifier != 'C';"""


def read_query(db_file):
    # Create a connection to the database
    conn = sqlite3.connect(f'database/{db_file}')
    # Iread the query into a pd.DataFrame
    df = pd.read_sql_query(query, conn)
    # close the connection
    conn.close()
    return df



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, help='SQLite database name')
    args = parser.parse_args()

    df = read_query(args.db)
    cr = classification_report(y_true=df.true_fallacy_text, y_pred=df.pred_fallacy_text, zero_division=0.0, output_dict=True)
    #TODO: save dict as json file
    labels = list(cr.keys())[:-3]
    cr = classification_report(y_true=df.true_fallacy_text, y_pred=df.pred_fallacy_text, zero_division=0.0, output_dict=False)
    print(cr)
    ConfusionMatrixDisplay.from_predictions(y_true=df.true_fallacy_text, 
                                        y_pred=df.pred_fallacy_text,
                                        labels=labels,
                                        xticks_rotation='vertical',
                                        cmap='Blues',
                                        colorbar=False)
    #TODO: save ConfusionMatrixDisplay as pdf file