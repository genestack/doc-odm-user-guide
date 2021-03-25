# Roche pRed Curator Layers 4
# 
# This is the API for layer 4 of the Roche pRed project.  This swagger page describes the integrationCurator APIs.  Before carrying out any API calls you will need an API token. API tokens can be obtained under your profile within the Genestack software.  To try out calls in this swagger page:  1. Click the 'Authorize' button below to enter your API token 2. Scroll to the 'Parameters' section for the method you wish to try out and click the 'Try it out' button 3. Enter parameter values that you wish to try 4. Scroll to the bottom of the Parameters section and click the 'Execute' bar that appears  The server response will be in the section that follows.
# 
# API version: v0.1
# 

PreparationIntegrationApi <- R6::R6Class(
  'PreparationIntegrationApi',
  public = list(
    userAgent = "Swagger-Codegen/1.36.0-1/r",
    apiClient = NULL,
    initialize = function(apiClient){
      if (!missing(apiClient)) {
        self$apiClient <- apiClient
      }
      else {
        self$apiClient <- ApiClient$new()
      }
    },
    create_preparation_group_sample_group_link = function(source_id, target_id, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      body <- NULL
      urlPath <- "/integration/link/preparation/group/{sourceId}/to/sample/group/{targetId}"
      if (!missing(`source_id`)) {
        urlPath <- gsub(paste0("\\{", "sourceId", "\\}"), `source_id`, urlPath)
      }

      if (!missing(`target_id`)) {
        urlPath <- gsub(paste0("\\{", "targetId", "\\}"), `target_id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "POST",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        # void response, no need to return anything
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    create_preparation_sample_link = function(source_id, target_id, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      body <- NULL
      urlPath <- "/integration/link/preparation/{sourceId}/to/sample/{targetId}"
      if (!missing(`source_id`)) {
        urlPath <- gsub(paste0("\\{", "sourceId", "\\}"), `source_id`, urlPath)
      }

      if (!missing(`target_id`)) {
        urlPath <- gsub(paste0("\\{", "targetId", "\\}"), `target_id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "POST",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        # void response, no need to return anything
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    delete_preparation_group_sample_group_link = function(source_id, target_id, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      body <- NULL
      urlPath <- "/integration/link/preparation/group/{sourceId}/to/sample/group/{targetId}"
      if (!missing(`source_id`)) {
        urlPath <- gsub(paste0("\\{", "sourceId", "\\}"), `source_id`, urlPath)
      }

      if (!missing(`target_id`)) {
        urlPath <- gsub(paste0("\\{", "targetId", "\\}"), `target_id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "DELETE",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        # void response, no need to return anything
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    delete_preparation_sample_link = function(source_id, target_id, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      body <- NULL
      urlPath <- "/integration/link/preparation/{sourceId}/to/sample/{targetId}"
      if (!missing(`source_id`)) {
        urlPath <- gsub(paste0("\\{", "sourceId", "\\}"), `source_id`, urlPath)
      }

      if (!missing(`target_id`)) {
        urlPath <- gsub(paste0("\\{", "targetId", "\\}"), `target_id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "DELETE",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        # void response, no need to return anything
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    get_parents_by_study = function(id, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      body <- NULL
      urlPath <- "/integration/link/preparation/group/by/study/{id}"
      if (!missing(`id`)) {
        urlPath <- gsub(paste0("\\{", "id", "\\}"), `id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "GET",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        json <- httr::content(resp, "text", encoding = "UTF-8")
        if (json == "") {
          responseObject <- NULL
        } else {
          responseObject <- tryCatch(jsonlite::fromJSON(json), error=function(cond) { return(NULL) })
        }
        Response$new(responseObject, json, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    get_preparation_by_sample = function(id, returned_metadata_fields, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      if (!missing(`returned_metadata_fields`)) {
        queryParams['returnedMetadataFields'] <- returned_metadata_fields
      }

      body <- NULL
      urlPath <- "/integration/link/preparation/by/sample/{id}"
      if (!missing(`id`)) {
        urlPath <- gsub(paste0("\\{", "id", "\\}"), `id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "GET",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        json <- httr::content(resp, "text", encoding = "UTF-8")
        if (json == "") {
          responseObject <- NULL
        } else {
          responseObject <- tryCatch(jsonlite::fromJSON(json), error=function(cond) { return(NULL) })
        }
        Response$new(responseObject, json, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    get_preparation_links_to_samples = function(id, page_limit, page_offset, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      if (!missing(`page_limit`)) {
        queryParams['pageLimit'] <- page_limit
      }

      if (!missing(`page_offset`)) {
        queryParams['pageOffset'] <- page_offset
      }

      body <- NULL
      urlPath <- "/integration/link/preparation/preparations-to-samples/by/group/{id}"
      if (!missing(`id`)) {
        urlPath <- gsub(paste0("\\{", "id", "\\}"), `id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "GET",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        json <- httr::content(resp, "text", encoding = "UTF-8")
        if (json == "") {
          responseObject <- NULL
        } else {
          responseObject <- tryCatch(jsonlite::fromJSON(json), error=function(cond) { return(NULL) })
        }
        Response$new(responseObject, json, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    },
    get_preparations_by_samples = function(filter, query, search_specific_terms, page_limit, page_offset, returned_metadata_fields, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      if (!missing(`filter`)) {
        queryParams['filter'] <- filter
      }

      if (!missing(`query`)) {
        queryParams['query'] <- query
      }

      if (!missing(`search_specific_terms`)) {
        queryParams['searchSpecificTerms'] <- search_specific_terms
      }

      if (!missing(`page_limit`)) {
        queryParams['pageLimit'] <- page_limit
      }

      if (!missing(`page_offset`)) {
        queryParams['pageOffset'] <- page_offset
      }

      if (!missing(`returned_metadata_fields`)) {
        queryParams['returnedMetadataFields'] <- returned_metadata_fields
      }

      body <- NULL
      urlPath <- "/integration/link/preparations/by/samples"
      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "GET",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        json <- httr::content(resp, "text", encoding = "UTF-8")
        if (json == "") {
          responseObject <- NULL
        } else {
          responseObject <- tryCatch(jsonlite::fromJSON(json), error=function(cond) { return(NULL) })
        }
        Response$new(responseObject, json, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", "null", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", "null", resp)
      }

    }
  )
)

#' Create links between samples and preparations
#'
#' @param source_id The ID (accession) of the preparation group object
#' @param target_id The ID (accession) of the sample group object
#'
#' @export PreparationIntegrationApi_create_preparation_group_sample_group_link
#'
PreparationIntegrationApi_create_preparation_group_sample_group_link <- function(source_id, target_id, ...) {
  PreparationIntegrationApi$new()$create_preparation_group_sample_group_link(source_id, target_id, ...)
}

#' Create a link between a preparation and a sample
#'
#' @param source_id The ID (accession) of the preparation object
#' @param target_id The ID (accession) of the sample object
#'
#' @export PreparationIntegrationApi_create_preparation_sample_link
#'
PreparationIntegrationApi_create_preparation_sample_link <- function(source_id, target_id, ...) {
  PreparationIntegrationApi$new()$create_preparation_sample_link(source_id, target_id, ...)
}

#' Delete links between samples and preparations related to the specified group
#'
#' @param source_id The ID (accession) of the preparation group object
#' @param target_id The ID (accession) of the sample group object
#'
#' @export PreparationIntegrationApi_delete_preparation_group_sample_group_link
#'
PreparationIntegrationApi_delete_preparation_group_sample_group_link <- function(source_id, target_id, ...) {
  PreparationIntegrationApi$new()$delete_preparation_group_sample_group_link(source_id, target_id, ...)
}

#' Delete a link between a preparation and a sample
#'
#' @param source_id The ID (accession) of the preparation object
#' @param target_id The ID (accession) of the sample object
#'
#' @export PreparationIntegrationApi_delete_preparation_sample_link
#'
PreparationIntegrationApi_delete_preparation_sample_link <- function(source_id, target_id, ...) {
  PreparationIntegrationApi$new()$delete_preparation_sample_link(source_id, target_id, ...)
}

#' Retrieve group metadata by querying study ID (accession)
#'
#' @param id Unique identifier (accession) of the object.
#'
#' @export PreparationIntegrationApi_get_parents_by_study
#'
PreparationIntegrationApi_get_parents_by_study <- function(id, ...) {
  PreparationIntegrationApi$new()$get_parents_by_study(id, ...)
}

#' Retrieve preparation metadata by querying related sample ID (accession)
#'
#' @param id Unique identifier (accession) of the object.
#' @param returned_metadata_fields The parameter defines amount of metadata attributes to return:  1. \code{template} - return metadata attributes according to applied template, if object doesn’t have applied template default template will be used. This is the default for User endpoints. 2. \code{all} - return all metadata attributes with values and null attributes, if they are present in the applied template. This is the default for Curator endpoints.
#'
#' @export PreparationIntegrationApi_get_preparation_by_sample
#'
PreparationIntegrationApi_get_preparation_by_sample <- function(id, returned_metadata_fields, ...) {
  PreparationIntegrationApi$new()$get_preparation_by_sample(id, returned_metadata_fields, ...)
}

#' Retrieve run-sample pairs by group id. Pagination is based on unique preparations, not unique pairs.
#'
#' @param id Unique identifier (accession) of the object.
#' @param page_limit Maximum number of results to return. This value must be between 0 and 2000 (inclusive).
#' @param page_offset Show the page {pageOffset+1} results from the start of the results. E.g. 100 will show a page of results  starting from the 101st result. The default value is 0.
#'
#' @export PreparationIntegrationApi_get_preparation_links_to_samples
#'
PreparationIntegrationApi_get_preparation_links_to_samples <- function(id, page_limit, page_offset, ...) {
  PreparationIntegrationApi$new()$get_preparation_links_to_samples(id, page_limit, page_offset, ...)
}

#' Retrieve preparation metadata by querying related samples
#'
#' @param filter Filter by sample metadata (key-value metadata pair(s)). E.g. \code{"Species or strain"="Homo sapiens"} 
#' @param query Search for objects via a full-text query over all sample metadata fields. E.g. \code{Clozapine}
#' @param search_specific_terms If the full-text query term is present in an RTS dictionary, enabling this parameter will modify the query to include child terms of the full-text query.  For example, the search query "Body fluid" can be expanded to include the term "Blood" (a child term of  "Body fluid") so files containing either "Body fluid" or  "Blood"  in their metadata will be returned in the search results.  The parent-child relationship is defined by the key "broaders"  in the dictionary.  If the full query term is not present in a dictionary then this parameter has no effect.
#' @param page_limit Maximum number of results to return. This value must be between 0 and 2000 (inclusive).
#' @param page_offset Show the page {pageOffset+1} results from the start of the results. E.g. 100 will show a page of results  starting from the 101st result. The default value is 0.
#' @param returned_metadata_fields The parameter defines amount of metadata attributes to return:  1. \code{template} - return metadata attributes according to applied template, if object doesn’t have applied template default template will be used. This is the default for User endpoints. 2. \code{all} - return all metadata attributes with values and null attributes, if they are present in the applied template. This is the default for Curator endpoints.
#'
#' @export PreparationIntegrationApi_get_preparations_by_samples
#'
PreparationIntegrationApi_get_preparations_by_samples <- function(filter, query, search_specific_terms, page_limit, page_offset, returned_metadata_fields, ...) {
  PreparationIntegrationApi$new()$get_preparations_by_samples(filter, query, search_specific_terms, page_limit, page_offset, returned_metadata_fields, ...)
}

