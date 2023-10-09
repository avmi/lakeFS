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


package io.lakefs.clients.api.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * CommPrefsInput
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen")
public class CommPrefsInput {
  public static final String SERIALIZED_NAME_EMAIL = "email";
  @SerializedName(SERIALIZED_NAME_EMAIL)
  private String email;

  public static final String SERIALIZED_NAME_FEATURE_UPDATES = "featureUpdates";
  @SerializedName(SERIALIZED_NAME_FEATURE_UPDATES)
  private Boolean featureUpdates;

  public static final String SERIALIZED_NAME_SECURITY_UPDATES = "securityUpdates";
  @SerializedName(SERIALIZED_NAME_SECURITY_UPDATES)
  private Boolean securityUpdates;


  public CommPrefsInput email(String email) {
    
    this.email = email;
    return this;
  }

   /**
   * the provided email
   * @return email
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "the provided email")

  public String getEmail() {
    return email;
  }


  public void setEmail(String email) {
    this.email = email;
  }


  public CommPrefsInput featureUpdates(Boolean featureUpdates) {
    
    this.featureUpdates = featureUpdates;
    return this;
  }

   /**
   * user preference to receive feature updates
   * @return featureUpdates
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "user preference to receive feature updates")

  public Boolean getFeatureUpdates() {
    return featureUpdates;
  }


  public void setFeatureUpdates(Boolean featureUpdates) {
    this.featureUpdates = featureUpdates;
  }


  public CommPrefsInput securityUpdates(Boolean securityUpdates) {
    
    this.securityUpdates = securityUpdates;
    return this;
  }

   /**
   * user preference to receive security updates
   * @return securityUpdates
  **/
  @javax.annotation.Nonnull
  @ApiModelProperty(required = true, value = "user preference to receive security updates")

  public Boolean getSecurityUpdates() {
    return securityUpdates;
  }


  public void setSecurityUpdates(Boolean securityUpdates) {
    this.securityUpdates = securityUpdates;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CommPrefsInput commPrefsInput = (CommPrefsInput) o;
    return Objects.equals(this.email, commPrefsInput.email) &&
        Objects.equals(this.featureUpdates, commPrefsInput.featureUpdates) &&
        Objects.equals(this.securityUpdates, commPrefsInput.securityUpdates);
  }

  @Override
  public int hashCode() {
    return Objects.hash(email, featureUpdates, securityUpdates);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CommPrefsInput {\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("    featureUpdates: ").append(toIndentedString(featureUpdates)).append("\n");
    sb.append("    securityUpdates: ").append(toIndentedString(securityUpdates)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

