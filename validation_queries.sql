-- 1. Check for Missing IDs or Amounts
SELECT * FROM transactions 
WHERE transaction_id IS NULL OR amount IS NULL;

-- 2. Find Duplicate Transactions
SELECT transaction_id, COUNT(*) as duplicate_count 
FROM transactions 
WHERE transaction_id IS NOT NULL 
GROUP BY transaction_id 
HAVING COUNT(*) > 1;

-- 3. Flag Unusual Values (Negative amounts or unusually high amounts)
SELECT * FROM transactions 
WHERE amount < 0 OR amount > 10000;
