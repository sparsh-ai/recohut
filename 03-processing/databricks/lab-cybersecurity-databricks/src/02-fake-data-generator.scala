// Databricks notebook source
// MAGIC %md 
// MAGIC ## Purpose 
// MAGIC -  This notebook generates systematically genated fake data and writes the data on the raw data storage
// MAGIC ### How to use these demo notebooks 
// MAGIC  1. run fake_data_generator
// MAGIC  2. run raw_to_bronze_job
// MAGIC  3. run bronze_to_silver_job
// MAGIC  4. run fake_data_generator if it is required to genarate more data  
// MAGIC  

// COMMAND ----------

// MAGIC %run ./lakehouse_pipeline_demo_0_sample_schema

// COMMAND ----------

import java.io._
import java.util.zip._
import scala.io.Source
import com.google.gson.Gson
import java.nio.file.Files
import java.nio.file.Paths
import java.util.UUID

Files.createDirectories(Paths.get("/tmp/crowstrike/data"))

def genarateFakeGzFile (numpberOfCopies:Int , targetPath:String ) ={
  val LocalPath="/tmp/crowstrike/data" 
  val fileName = UUID.randomUUID().toString.replace("-","") + ".gz"
  val fullFilePath = LocalPath + "/" + fileName
  var lines= ""
  val gson = new Gson

  for( i <- 1 until numpberOfCopies){
    
      lines += gson.toJson(new AgentConnect) + "\n"
      lines += gson.toJson(new AgentOnline) + "\n"
      lines += gson.toJson(new HostInfo) + "\n"
      lines += gson.toJson(new PrivilegedProcessHandleFromUnsignedModule) + "\n"
      lines += gson.toJson(new RegKeySecurityDecreasedFromUnsignedModule) + "\n"
      lines += gson.toJson(new CustomIOABasicProcessDetectionInfoEvent ) + "\n"
      lines += gson.toJson(new InjectedThreadFromUnsignedModule ) +  "\n"
      lines += gson.toJson(new ModuleBlockedEventWithPatternId ) + "\n"
      lines += gson.toJson(new UpdateManifestDownloadComplete ) + "\n"
      lines += gson.toJson(new InstallServiceDownloadComplete ) + "\n"
      lines += gson.toJson(new FileSystemOperationDetectInfo ) + "\n"
      lines += gson.toJson(new DocumentProgramInjectedThread ) + "\n"
      lines += gson.toJson(new WfpFilterTamperingFilterAdded ) + "\n"
      lines += gson.toJson(new SuspiciousCreateSymbolicLink ) + "\n"
      lines += gson.toJson(new RemoteCommandAcknowledgment ) + "\n"
      lines += gson.toJson(new NetworkContainmentCompleted) + "\n"
  }
  
val output = new FileOutputStream(fullFilePath) 
try {
  val writer = new OutputStreamWriter(new GZIPOutputStream(output), "UTF-8")
  try writer.write(lines)
  finally writer.close()
} finally output.close()
  
  val targetFileName = targetPath + fileName
  dbutils.fs.cp("file:" +fullFilePath , targetFileName )
  dbutils.fs.rm(fullFilePath)

}


// COMMAND ----------

val targetPath = "dbfs:/tmp/raw/data/"
 //one copy from each type is has 4k filesize 
1 to 10 foreach { _ => genarateFakeGzFile (100, targetPath)
                
               }

dbutils.fs.ls ("file:/tmp/crowstrike/data")
