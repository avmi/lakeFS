/*
 * lakeFS API
 *
 * lakeFS HTTP API
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: services@treeverse.io
 * Generated by: https://openapi-generator.tech
 */

use crate::models;

#[derive(Clone, Default, Debug, PartialEq, Serialize, Deserialize)]
pub struct ExternalPrincipalList {
    #[serde(rename = "pagination")]
    pub pagination: Box<models::Pagination>,
    #[serde(rename = "results")]
    pub results: Vec<models::ExternalPrincipal>,
}

impl ExternalPrincipalList {
    pub fn new(pagination: models::Pagination, results: Vec<models::ExternalPrincipal>) -> ExternalPrincipalList {
        ExternalPrincipalList {
            pagination: Box::new(pagination),
            results,
        }
    }
}
