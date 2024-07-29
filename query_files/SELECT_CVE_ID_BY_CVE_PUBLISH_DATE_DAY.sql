-- SELECT_CVE_ID_BY_CVE_PUBLISH_DATE_DAY
SELECT CVE_ID
FROM CVE
WHERE strftime('%d', PUBLISH_DATE) = ?; -- формат дня должен быть 'DD'