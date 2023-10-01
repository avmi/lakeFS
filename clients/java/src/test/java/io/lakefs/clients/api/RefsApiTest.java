/*
 * lakeFS API
 * lakeFS HTTP API
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package io.lakefs.clients.api;

import io.lakefs.clients.api.ApiException;
import io.lakefs.clients.api.model.CommitList;
import io.lakefs.clients.api.model.DiffList;
import io.lakefs.clients.api.model.Error;
import io.lakefs.clients.api.model.FindMergeBaseResult;
import io.lakefs.clients.api.model.Merge;
import io.lakefs.clients.api.model.MergeResult;
import org.junit.Test;
import org.junit.Ignore;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for RefsApi
 */
@Ignore
public class RefsApiTest {

    private final RefsApi api = new RefsApi();

    
    /**
     * diff references
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void diffRefsTest() throws ApiException {
        String repository = null;
        String leftRef = null;
        String rightRef = null;
        String after = null;
        Integer amount = null;
        String prefix = null;
        String delimiter = null;
        String type = null;
                DiffList response = api.diffRefs(repository, leftRef, rightRef, after, amount, prefix, delimiter, type);
        // TODO: test validations
    }
    
    /**
     * find the merge base for 2 references
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void findMergeBaseTest() throws ApiException {
        String repository = null;
        String sourceRef = null;
        String destinationBranch = null;
                FindMergeBaseResult response = api.findMergeBase(repository, sourceRef, destinationBranch);
        // TODO: test validations
    }
    
    /**
     * get commit log from ref. If both objects and prefixes are empty, return all commits.
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void logCommitsTest() throws ApiException {
        String repository = null;
        String ref = null;
        String after = null;
        Integer amount = null;
        List<String> objects = null;
        List<String> prefixes = null;
        Boolean limit = null;
        Boolean firstParent = null;
                CommitList response = api.logCommits(repository, ref, after, amount, objects, prefixes, limit, firstParent);
        // TODO: test validations
    }
    
    /**
     * merge references
     *
     * 
     *
     * @throws ApiException
     *          if the Api call fails
     */
    @Test
    public void mergeIntoBranchTest() throws ApiException {
        String repository = null;
        String sourceRef = null;
        String destinationBranch = null;
        Merge merge = null;
                MergeResult response = api.mergeIntoBranch(repository, sourceRef, destinationBranch, merge);
        // TODO: test validations
    }
    
}
