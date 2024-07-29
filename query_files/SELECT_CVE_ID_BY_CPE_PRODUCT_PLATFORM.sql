-- SELECT_CVE_ID_BY_CPE_PRODUCT_PLATFORM
SELECT CVE.CVE_ID
FROM CVE
JOIN CVE_has_CPE_GROUP ON CVE.CVE_ID = CVE_has_CPE_GROUP.CVE_ID
JOIN CPE_GROUP_has_CPE ON CVE_has_CPE_GROUP.CPE_GROUP_ID = CPE_GROUP_has_CPE.CPE_GROUP_ID
JOIN CPE ON CPE_GROUP_has_CPE.CPE_ID = CPE.CPE_ID
WHERE CPE.CPE_PRODUCT_PLATFORM = ?;