curl -X POST "https://occam.genestack.com/frontend/rs/genestack/expressionCurator/default-released/expression/gct" -H  "accept: application/json" -H  "Genestack-API-Token: <token>" -H  "Content-Type: application/json" -d "{  \"link\": \"https://bio-test-data.s3.amazonaws.com/Research_Model_BR-205/Test_RM_g.gct\",  \"metadataLink\": \"https://bio-test-data.s3.amazonaws.com/Research_Model_BR-205/Test_RM_g.gct.tsv\"}"
