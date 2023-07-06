import argparse
import sqlite3
import pandas as pd

def create_database(csv_file, db_file):
    # Create a connection to the database
    conn = sqlite3.connect(f'database/{db_file}')
    cursor = conn.cursor()

    # Create the Claims table
    cursor.execute('''
        DROP TABLE IF EXISTS Claims
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Claims (
            claims_id INTEGER PRIMARY KEY,
            code TEXT,
            claims_text TEXT,
            argument_validity BOOLEAN
        )
    ''')

    # Create the True_Premises table
    cursor.execute('''
        DROP TABLE IF EXISTS True_Premises
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS True_Premises (
            premise_id INTEGER PRIMARY KEY,
            claims_id INTEGER,
            premise TEXT,
            is_hidden BOOLEAN,
            premise_identifier TEXT,
            FOREIGN KEY (claims_id) REFERENCES Claims (claims_id)
        )
    ''')

    # Create the Pred_Premises table
    cursor.execute('''
        DROP TABLE IF EXISTS Pred_Premises
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pred_Premises (
            premise_id INTEGER PRIMARY KEY,
            claims_id INTEGER,
            premise TEXT,
            is_hidden BOOLEAN,
            premise_identifier TEXT,
            FOREIGN KEY (claims_id) REFERENCES Claims (claims_id)
        )
    ''')

    # Create the True_Fallacies table
    cursor.execute('''
        DROP TABLE IF EXISTS True_Fallacies
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS True_Fallacies (
            fallacy_id INTEGER PRIMARY KEY,
            premise_id INTEGER,
            fallacy_text TEXT,
            FOREIGN KEY (premise_id) REFERENCES True_Premises (premise_id)
        )
    ''')

    # Create the Pred_Fallacies table
    cursor.execute('''
        DROP TABLE IF EXISTS Pred_Fallacies
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Pred_Fallacies (
            fallacy_id INTEGER PRIMARY KEY,
            premise_id INTEGER,
            fallacy_text TEXT,
            fallacy_validity TEXT,
            FOREIGN KEY (premise_id) REFERENCES Pred_Premises (premise_id)
        )
    ''')

    # Create the LLM_Validity table
    cursor.execute('''
        DROP TABLE IF EXISTS LLM_Validity
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LLM_Validity (
            validity_id INTEGER PRIMARY KEY,
            claims_id INTEGER,
            validity_text TEXT,
            argument_validity BOOLEAN,
            FOREIGN KEY (claims_id) REFERENCES Claims (claims_id)
        )
    ''')


    # Read Deconstructed CARDS claims
    jc = pd.read_csv(csv_file)


    for i, row in enumerate(jc.itertuples()):
        code = row[0]
        claim = row[3]
        premises = row[8]
        hidden_premises = row[9]
        fallacies = row[10]

        # Insert into Claims table
        cursor.execute('''
            INSERT INTO Claims (code, claims_text, argument_validity)
            VALUES (?, ?, ?)''', 
            (code, claim, isinstance(hidden_premises, str)))
        
        claims_id = cursor.lastrowid

        for premise in premises.split('\n'):
            idp, txt = premise.split(': ')
            is_hidden = False

            # Insert into True_Premises table
            cursor.execute('''
            INSERT INTO True_Premises (claims_id, premise, is_hidden, premise_identifier)
            VALUES (?, ?, ?, ?)''',
            (claims_id, txt.strip(), is_hidden, idp.strip()))

            premise_id = cursor.lastrowid

            for fallacy in fallacies.split('\n'):
                idf, txt = fallacy.split(': ')

                if idp == idf:
                    
                    # Insert into True_Fallacies table
                    cursor.execute('''
                    INSERT INTO True_Fallacies (premise_id, fallacy_text)
                    VALUES (?, ?)''',
                    (premise_id, txt.lower()))

        if isinstance(hidden_premises, str):
            for premise in hidden_premises.split('\n'):
                idp, txt = premise.split(': ')
                is_hidden = True

                # Insert into True_Premises table
                cursor.execute('''
                INSERT INTO True_Premises (claims_id, premise, is_hidden, premise_identifier)
                VALUES (?, ?, ?, ?)''',
                (claims_id, txt.strip(), is_hidden, idp.strip()))

                premise_id = cursor.lastrowid

                for fallacy in fallacies.split('\n'):
                    idf, txt = fallacy.split(': ')

                    if idp == idf:
                        
                        # Insert into True_Fallacies table
                        cursor.execute('''
                        INSERT INTO True_Fallacies (premise_id, fallacy_text)
                        VALUES (?, ?)''',
                        (premise_id, txt.lower()))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', default='datasets/Deconstructed CARDS claims - Sheet1.csv', type=str ,help='Path to the CSV file')
    parser.add_argument('--db', type=str, help='SQLite database name')
    args = parser.parse_args()

    create_database(args.csv, args.db)