--- This script was used to generate the data for the dataset
USE
    udb_1;
SELECT
    ii.ID AS "ItemID",
    MD5(ii.EstNum) AS "UUID",
    i.EstDesc AS "Description",
    ii.JobDesc AS "ItemDescription"
FROM
    InvoiceItems ii
LEFT JOIN Invoices i ON
    i.EstNum = ii.EstNum
WHERE
    i.Deleted = 0 AND i.Private = 0 AND ii.InvType = "Labor"
