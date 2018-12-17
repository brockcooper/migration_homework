/*
Create the new account table and make the Foreign Key reference
Use the ON DELETE RESTRICT so the DB will force you to delete
accounts associtated with a company before deleting those companies
*/
CREATE TABLE accounts (
  id BIGSERIAL PRIMARY KEY,
  company_id INTEGER REFERENCES companies(id) ON DELETE RESTRICT
);

/*
Fill the account table with the company ids
Since we set up the primary key in the first step,
we only need to bring in the company id and the account id
will populate automatically
*/
INSERT INTO accounts (company_id)
  SELECT id
  FROM companies;

-- Create the new column in daily balances and use the delete restrict again
ALTER TABLE daily_balances
  ADD COLUMN account_id BIGINT,
  ADD CONSTRAINT fk_account_id
    FOREIGN KEY (account_id)
    REFERENCES accounts(id) ON DELETE RESTRICT;

-- Fill the new account_id column with a join to account table on company_id
UPDATE daily_balances d
  SET d.account_id = a.id
  FROM accounts a
  WHERE a.company_id = d.company_id;

-- Drop the company_id table
ALTER TABLE daily_balances
  DROP COLUMN company_id;
