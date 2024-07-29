-- SELECT_CVE_ID_BY_CVE_PUBLISH_DATE_MONTH
SELECT CVE_ID
FROM CVE
WHERE strftime('%m', PUBLISH_DATE) = ?; -- формат месяца должен быть 'MM'
