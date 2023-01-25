// Databricks notebook source
// MAGIC %md 
// MAGIC ## This notebook generates a sample crowstrike data payload
// MAGIC   - please be aware that the data is generated from the notebook is fake and shouldn't be used for any research
// MAGIC   - We don't need to run this notebook, but it will be used by athor notebooks in this package 

// COMMAND ----------

import java.time._
import com.google.gson.Gson

def randomIp():String ={

  val r = scala.util.Random
  r.nextInt(256) + "." + r.nextInt(256) + "." + r.nextInt(256) + "." + r.nextInt(256)
}
def randomVersion():String ={
  val r = scala.util.Random
  r.nextInt(10) + "." + r.nextInt(10) + "." + r.nextInt(10)
}
def generateTimestamp():String = {
 Instant.now.getEpochSecond.toString
}
def randomDigit():String = {
  scala.util.Random.nextInt(10).toString
}
def uuid():String = {
  java.util.UUID.randomUUID.toString
}
def randomName():String = {
  "test" + scala.util.Random.nextInt(1000).toString
}
case class AgentConnect (
                          ConfigBuild:String= "1.0.1",
                          ConfigIDBase:String = "1.0." ,
                          ConfigIDBuild:String = randomVersion() ,
                          ConfigIDPlatform:String = randomVersion() ,
                          ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                          ConfigurationVersion:String = "1.0.0.1" ,
                          ConnectTime:String = Instant.now.getEpochSecond.toString ,
                          ConnectType:String = "1" ,
                          ConnectionCipher:String = "1" ,
                          ConnectionCipherStrength:String = randomDigit ,
                          ConnectionExchange:String = randomDigit ,
                          ConnectionExchangeStrength:String = randomDigit ,
                          ConnectionHash:String = randomDigit ,
                          ConnectionHashStrength:String = randomDigit ,
                          ConnectionProtocol:String = "HTTPS" ,
                          EffectiveTransmissionClass:String = randomDigit ,
                          Entitlements:String = randomDigit ,
                          FailedConnectCount:String = "10" ,
                          NetworkContainmentState:String = "active" ,
                          PreviousConnectTime:String = Instant.now.getEpochSecond.toString ,
                          ProvisionState:String = "1" ,
                          VerifiedCertificate:String = "true" ,
                          aid:String = scala.util.Random.nextInt(1000).toString  ,
                          aip:String = randomIp() ,
                          cid:String = "1" ,
                          event_platform:String = "mac" ,
                          event_simpleName:String = "AgentConnect" ,
                          id:String = scala.util.Random.nextInt(1000).toString  ,
                          name:String = randomName ,
                          timestamp:String =  generateTimestamp()
                        )


case class AgentOnline (
                         AgentLoadFlags:String = uuid ,
                         AgentLocalTime:String = generateTimestamp,
                         AgentVersion:String = randomVersion() ,
                         BaseTime:String = generateTimestamp,
                         BiosManufacturer:String = uuid ,
                         BiosReleaseDate:String = generateTimestamp ,
                         BiosVersion:String = randomVersion() ,
                         Bootid:String = scala.util.Random.nextInt(1000).toString  ,
                         BootStatusDataAabEnabled:String = uuid ,
                         BootStatusDataBootAttemptCount:String = uuid ,
                         BootStatusDataBootGood:String = uuid ,
                         BootStatusDataBootShutdown:String = uuid ,
                         ChasisManufacturer:String = uuid ,
                         ChassisType:String = uuid ,
                         ComputerName:String = randomName,
                         ConfigBuild:String = "1.0.0." ,
                         ConfigIDBase:String = "1.0." ,
                         ConfigIDBuild:String = randomVersion() ,
                         ConfigIDPlatform:String = uuid ,
                         ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                         ConfigurationVersion:String = "1.0.0.1" ,
                         ContextTimeStamp:String = generateTimestamp ,
                         CpuFeaturesMask:String = uuid ,
                         CpuSignature:String = uuid ,
                         CpuVendor:String = uuid ,
                         EffectiveTransmissionClass:String = randomDigit ,
                         Entitlements:String = randomDigit ,
                         MdmDeviceid:String = scala.util.Random.nextInt(1000).toString  ,
                         MicrocodeSignature:String = uuid ,
                         MoboManufacturer:String = uuid ,
                         MoboProductName:String = randomName,
                         NorthBridgeDeviceid:String = scala.util.Random.nextInt(1000).toString  ,
                         NorthBridgeVendorid:String = scala.util.Random.nextInt(1000).toString  ,
                         PlatformSecuritySettings:String = uuid ,
                         PlatformSecurityStatus:String = "COMPLETE" ,
                         ProvisionState:String = randomDigit,
                         SideChannelMitigationFlags:String = uuid ,
                         SouthBridgeDeviceid:String = scala.util.Random.nextInt(1000).toString  ,
                         SouthBridgeVendorid:String = scala.util.Random.nextInt(1000).toString  ,
                         SystemManufacturer:String = uuid ,
                         SystemProductName:String = randomName,
                         SystemSerialNumber:String = uuid ,
                         SystemSku:String = uuid ,
                         TargetFileName:String = randomName,
                         TpmFirmwareVersion:String = randomVersion() ,
                         TpmManufacturer:String = uuid ,
                         TpmProductName:String = randomName,
                         TpmSpecification:String = uuid ,
                         TpmType:String = uuid ,
                         aid:String = scala.util.Random.nextInt(1000).toString  ,
                         aip:String = randomIp() ,
                         cid:String = "1" ,
                         event_platform:String = "mac" ,
                         event_simpleName:String = "AgentOnline" ,
                         id:String = scala.util.Random.nextInt(1000).toString  ,
                         name:String = randomName ,
                         timestamp:String =  generateTimestamp()
                       )


case class HostInfo (
                      BootArgs:String = randomVersion() ,
                      ConfigBuild:String = "1.0.0." ,
                      ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                      DcName:String = randomName,
                      EffectiveTransmissionClass:String = randomDigit ,
                      Entitlements:String = randomDigit ,
                      MachineDn:String = uuid ,
                      MachineDomain:String = uuid ,
                      SIPIsEnabled:String = uuid ,
                      SiteName:String = randomName,
                      aid:String = scala.util.Random.nextInt(1000).toString  ,
                      aip:String = randomIp() ,
                      cid:String = "1" ,
                      event_platform:String = "mac" ,
                      event_simpleName:String = "HostInfo" ,
                      id:String = scala.util.Random.nextInt(1000).toString  ,
                      name:String = randomName ,
                      timestamp:String =  generateTimestamp()
                    )

case class PrivilegedProcessHandleFromUnsignedModule (
                                                       Certificate:String = uuid ,
                                                       ConfigBuild:String = "1.0.0." ,
                                                       ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                                       ContextProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       ContextThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       ContextTimeStamp:String = generateTimestamp ,
                                                       DesiredAccess:String = uuid ,
                                                       EffectiveTransmissionClass:String = randomDigit ,
                                                       Entitlements:String = randomDigit ,
                                                       ExtendedKeyUsages:String = uuid ,
                                                       FileSigningTime:String = generateTimestamp,
                                                       HandleCreated:String = uuid ,
                                                       ImageFileName:String = randomName,
                                                       Object1Name:String = randomName,
                                                       Object1Type:String = uuid ,
                                                       PublicKey1:String = uuid ,
                                                       PublicKey2:String = uuid ,
                                                       PublicKey3:String = uuid ,
                                                       PublicKey4:String = uuid ,
                                                       PublicKeys:String = uuid ,
                                                       SHA256HashData:String = uuid ,
                                                       SignInfoFlags:String = uuid ,
                                                       Status:String = "COMPLETE" ,
                                                       TargetProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       Treeid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       aid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       aip:String = randomIp() ,
                                                       cid:String = "1" ,
                                                       event_platform:String = "mac" ,
                                                       event_simpleName:String = "PrivilegedProcessHandleFromUnsignedModule" ,
                                                       id:String = scala.util.Random.nextInt(1000).toString  ,
                                                       name:String = randomName ,
                                                       timestamp:String =  generateTimestamp())


case class RegKeySecurityDecreasedFromUnsignedModule (
                                                       Authenticationid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       Certificate:String = uuid ,
                                                       ConfigBuild:String = "1.0.0." ,
                                                       ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                                       ContextProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       ContextThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       ContextTimeStamp:String = generateTimestamp ,
                                                       EffectiveTransmissionClass:String = randomDigit ,
                                                       Entitlements:String = randomDigit ,
                                                       ExtendedKeyUsages:String = uuid ,
                                                       FileSigningTime:String = generateTimestamp,
                                                       ImageFileName:String = randomName,
                                                       KeyObject:String = uuid ,
                                                       PublicKey1:String = uuid ,
                                                       PublicKey2:String = uuid ,
                                                       PublicKey3:String = uuid ,
                                                       PublicKey4:String = uuid ,
                                                       PublicKeys:String = uuid ,
                                                       RegKeyChangeType:String = uuid ,
                                                       RegKeyNewUser1:String = uuid ,
                                                       RegKeyNewUser3:String = uuid ,
                                                       RegKeyNewUserAccessMask1:String = uuid ,
                                                       RegKeyNewUserAccessMask3:String = uuid ,
                                                       RegKeyPermissionChangedAccessMaskDifference2:String = uuid ,
                                                       RegKeyPermissionChangedUser2:String = uuid ,
                                                       RegObjectName:String = randomName,
                                                       RegOperationType:String = uuid ,
                                                       RegPostObjectName:String = randomName,
                                                       SHA256HashData:String = uuid ,
                                                       SignInfoFlags:String = uuid ,
                                                       Status:String = "COMPLETE" ,
                                                       TokenType:String = uuid ,
                                                       aid:String = scala.util.Random.nextInt(1000).toString  ,
                                                       aip:String = randomIp() ,
                                                       cid:String = "1" ,
                                                       event_platform:String = "mac" ,
                                                       event_simpleName:String = "RegKeySecurityDecreasedFromUnsignedModule" ,
                                                       id:String = scala.util.Random.nextInt(1000).toString  ,
                                                       name:String = randomName ,
                                                       timestamp:String =  generateTimestamp())


case class CustomIOABasicProcessDetectionInfoEvent (
                                                     CommandLine:String = uuid ,
                                                     ConfigBuild:String = "1.0.0." ,
                                                     ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                                     ContextTimeStamp:String = generateTimestamp ,
                                                     EffectiveTransmissionClass:String = randomDigit ,
                                                     Entitlements:String = randomDigit ,
                                                     GrandparentCommandLine:String = uuid ,
                                                     GrandparentImageFileName:String = randomName,
                                                     ImageFileName:String = randomName,
                                                     ParentCommandLine:String = uuid ,
                                                     ParentImageFileName:String = randomName,
                                                     Patternid:String = scala.util.Random.nextInt(1000).toString  ,
                                                     TargetProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                                     TemplateDisposition:String = uuid ,
                                                     TemplateInstanceid:String = scala.util.Random.nextInt(1000).toString  ,
                                                     TemplateInstanceVersion:String = randomVersion() ,
                                                     aid:String = scala.util.Random.nextInt(1000).toString  ,
                                                     aip:String = randomIp() ,
                                                     cid:String = "1" ,
                                                     event_platform:String = "mac" ,
                                                     event_simpleName:String = "CustomIOABasicProcessDetectionInfoEvent" ,
                                                     id:String = scala.util.Random.nextInt(1000).toString  ,
                                                     name:String = randomName ,
                                                     timestamp:String =  generateTimestamp())


case class InjectedThreadFromUnsignedModule (
                                              Certificate:String = uuid ,
                                              ConfigBuild:String = "1.0.0." ,
                                              ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                              ContextProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                              ContextThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                              ContextTimeStamp:String = generateTimestamp ,
                                              EffectiveTransmissionClass:String = randomDigit ,
                                              Entitlements:String = randomDigit ,
                                              ExtendedKeyUsages:String = uuid ,
                                              FileSigningTime:String = generateTimestamp,
                                              ImageFileName:String = randomName,
                                              InjectedThreadFlag:String = uuid ,
                                              PublicKey1:String = uuid ,
                                              PublicKey2:String = uuid ,
                                              PublicKey3:String = uuid ,
                                              PublicKey4:String = uuid ,
                                              PublicKeys:String = uuid ,
                                              RawProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                              RawThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                              SHA256HashData:String = uuid ,
                                              SignInfoFlags:String = uuid ,
                                              SourceThreadStartAddress:String = uuid ,
                                              TargetProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                              TargetThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                              ThreadStartAddress:String = uuid ,
                                              ThreadStartContext:String = uuid ,
                                              Treeid:String = scala.util.Random.nextInt(1000).toString  ,
                                              aid:String = scala.util.Random.nextInt(1000).toString  ,
                                              aip:String = randomIp() ,
                                              cid:String = "1" ,
                                              event_platform:String = "mac" ,
                                              event_simpleName:String = "InjectedThreadFromUnsignedModule" ,
                                              id:String = scala.util.Random.nextInt(1000).toString  ,
                                              name:String = randomName ,
                                              timestamp:String =  generateTimestamp())


case class ModuleBlockedEventWithPatternId (
                                             ConfigBuild:String = "1.0.0." ,
                                             ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                             ContextTimeStamp:String = generateTimestamp ,
                                             EffectiveTransmissionClass:String = randomDigit ,
                                             Entitlements:String = randomDigit ,
                                             MD5HashData:String = uuid ,
                                             Patternid:String = scala.util.Random.nextInt(1000).toString  ,
                                             SHA256HashData:String = uuid ,
                                             Sessionid:String = scala.util.Random.nextInt(1000).toString  ,
                                             TargetFileName:String = randomName,
                                             TargetProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                             TemplateDisposition:String = uuid ,
                                             TemplateInstanceid:String = scala.util.Random.nextInt(1000).toString  ,
                                             TemplateInstanceVersion:String = randomVersion() ,
                                             aid:String = scala.util.Random.nextInt(1000).toString  ,
                                             aip:String = randomIp() ,
                                             cid:String = "1" ,
                                             event_platform:String = "mac" ,
                                             event_simpleName:String = "ModuleBlockedEventWithPatternId" ,
                                             id:String = scala.util.Random.nextInt(1000).toString  ,
                                             name:String = randomName ,
                                             timestamp:String =  generateTimestamp())




case class UpdateManifestDownloadComplete (
                                            CloudErrorCode:String = uuid ,
                                            ConfigBuild:String = "1.0.0." ,
                                            ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                            EffectiveTransmissionClass:String = randomDigit ,
                                            Entitlements:String = randomDigit ,
                                            ErrorText:String = uuid ,
                                            _id:String = scala.util.Random.nextInt(1000).toString  ,
                                            SHA256HashData:String = uuid ,
                                            Status:String = "COMPLETE" ,
                                            TargetFileName:String = randomName,
                                            aid:String = scala.util.Random.nextInt(1000).toString  ,
                                            aip:String = randomIp() ,
                                            cid:String = "1" ,
                                            event_platform:String = "mac" ,
                                            event_simpleName:String = "UpdateManifestDownloadComplete" ,
                                            id:String = scala.util.Random.nextInt(1000).toString  ,
                                            name:String = randomName ,
                                            timestamp:String =  generateTimestamp())


case class InstallServiceDownloadComplete (
                                            CloudErrorCode:String = uuid ,
                                            ConfigBuild:String = "1.0.0." ,
                                            ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                            EffectiveTransmissionClass:String = randomDigit ,
                                            Entitlements:String = randomDigit ,
                                            ErrorText:String = uuid ,
                                            _id:String = scala.util.Random.nextInt(1000).toString  ,
                                            SHA256HashData:String = uuid ,
                                            Status:String = "COMPLETE" ,
                                            TargetFileName:String = randomName,
                                            aid:String = scala.util.Random.nextInt(1000).toString  ,
                                            aip:String = randomIp() ,
                                            cid:String = "1" ,
                                            event_platform:String = "mac" ,
                                            event_simpleName:String = "InstallServiceDownloadComplete" ,
                                            id:String = scala.util.Random.nextInt(1000).toString  ,
                                            name:String = randomName ,
                                            timestamp:String =  generateTimestamp())





case class FileSystemOperationDetectInfo (
                                           CommandLine:String = uuid ,
                                           ConfigBuild:String = "1.0.0." ,
                                           ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                           ContextProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                           ContextTimeStamp:String = generateTimestamp ,
                                           EffectiveTransmissionClass:String = randomDigit ,
                                           Entitlements:String = randomDigit ,
                                           FileSystemOperationType:String = uuid ,
                                           FsOperationClassification:String = uuid ,
                                           FsOperationClassificationFlags:String = uuid ,
                                           ImageFileName:String = randomName,
                                           Patternid:String = scala.util.Random.nextInt(1000).toString  ,
                                           SourceFileName:String = randomName,
                                           TargetFileName:String = randomName,
                                           TemplateDisposition:String = uuid ,
                                           TemplateInstanceid:String = scala.util.Random.nextInt(1000).toString  ,
                                           aid:String = scala.util.Random.nextInt(1000).toString  ,
                                           aip:String = randomIp() ,
                                           cid:String = "1" ,
                                           event_platform:String = "mac" ,
                                           event_simpleName:String = "FileSystemOperationDetectInfo" ,
                                           id:String = scala.util.Random.nextInt(1000).toString  ,
                                           name:String = randomName ,
                                           timestamp:String =  generateTimestamp())


case class DocumentProgramInjectedThread (
                                           ConfigBuild:String = "1.0.0." ,
                                           ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                           ContextProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                           ContextThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                           ContextTimeStamp:String = generateTimestamp ,
                                           EffectiveTransmissionClass:String = randomDigit ,
                                           Entitlements:String = randomDigit ,
                                           InjectedThreadFlag:String = uuid ,
                                           RawProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                           RawThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                           SourceThreadStartAddress:String = uuid ,
                                           TargetProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                           TargetThreadid:String = scala.util.Random.nextInt(1000).toString  ,
                                           ThreadStartAddress:String = uuid ,
                                           ThreadStartContext:String = uuid ,
                                           UserThread:String = uuid ,
                                           aid:String = scala.util.Random.nextInt(1000).toString  ,
                                           aip:String = randomIp() ,
                                           cid:String = "1" ,
                                           event_platform:String = "mac" ,
                                           event_simpleName:String = "DocumentProgramInjectedThread" ,
                                           id:String = scala.util.Random.nextInt(1000).toString  ,
                                           name:String = randomName ,
                                           timestamp:String =  generateTimestamp())


case class WfpFilterTamperingFilterAdded (
                                           ConfigBuild:String = "1.0.0." ,
                                           ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                           ContextTimeStamp:String = generateTimestamp ,
                                           EffectiveTransmissionClass:String = randomDigit ,
                                           Entitlements:String = randomDigit ,
                                           ReferencedCalloutGuid:String = scala.util.Random.nextInt(1000).toString  ,
                                           ReferencedCalloutGuidAsString:String = uuid ,
                                           TamperFilterAction:String = uuid ,
                                           TamperFilterConditionCount:String = uuid ,
                                           TamperFilterFlags:String = uuid ,
                                           TamperFilterGuid:String = scala.util.Random.nextInt(1000).toString  ,
                                           TamperFilterGuidAsString:String = uuid ,
                                           TamperFilterId2:String = uuid ,
                                           TamperFilterSublayerWeight:String = uuid ,
                                           TamperFilterWeight:String = uuid ,
                                           aid:String = scala.util.Random.nextInt(1000).toString  ,
                                           aip:String = randomIp() ,
                                           cid:String = "1" ,
                                           event_platform:String = "mac" ,
                                           event_simpleName:String = "WfpFilterTamperingFilterAdded" ,
                                           id:String = scala.util.Random.nextInt(1000).toString  ,
                                           name:String = randomName ,
                                           timestamp:String =  generateTimestamp())


case class SuspiciousCreateSymbolicLink (
                                          CommandLine:String = uuid ,
                                          ConfigBuild:String = "1.0.0." ,
                                          ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                          ContextProcessid:String = scala.util.Random.nextInt(1000).toString  ,
                                          ContextTimeStamp:String = generateTimestamp ,
                                          DesiredAccess:String = uuid ,
                                          EffectiveTransmissionClass:String = randomDigit ,
                                          Entitlements:String = randomDigit ,
                                          ImageFileName:String = randomName,
                                          Patternid:String = scala.util.Random.nextInt(1000).toString  ,
                                          Status:String = "COMPLETE" ,
                                          SymbolicLinkName:String = randomName,
                                          SymbolicLinkTarget:String = uuid ,
                                          aid:String = scala.util.Random.nextInt(1000).toString  ,
                                          aip:String = randomIp() ,
                                          cid:String = "1" ,
                                          event_platform:String = "mac" ,
                                          event_simpleName:String = "SuspiciousCreateSymbolicLink" ,
                                          id:String = scala.util.Random.nextInt(1000).toString  ,
                                          name:String = randomName ,
                                          timestamp:String =  generateTimestamp())







case class RemoteCommandAcknowledgment (
                                         CloudRequestid:String = scala.util.Random.nextInt(1000).toString  ,
                                         CommandCode:String = uuid ,
                                         CommandName:String = randomName,
                                         CommandSequenceNumber:String = uuid ,
                                         CommandSequenceTotal:String = uuid ,
                                         ConfigBuild:String = "1.0.0." ,
                                         ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                         EffectiveTransmissionClass:String = randomDigit ,
                                         Entitlements:String = randomDigit ,
                                         aid:String = scala.util.Random.nextInt(1000).toString  ,
                                         aip:String = randomIp() ,
                                         cid:String = "1" ,
                                         event_platform:String = "mac" ,
                                         event_simpleName:String = "RemoteCommandAcknowledgment" ,
                                         id:String = scala.util.Random.nextInt(1000).toString  ,
                                         name:String = randomName ,
                                         timestamp:String =  generateTimestamp())


case class NetworkContainmentCompleted (
                                         CloudRequestid:String = scala.util.Random.nextInt(1000).toString  ,
                                         ConfigBuild:String = "1.0.0." ,
                                         ConfigStateHash:String = "1qscfrrfvgt6ytgghyythg" ,
                                         ContextTimeStamp:String = generateTimestamp ,
                                         EffectiveTransmissionClass:String = randomDigit ,
                                         Entitlements:String = randomDigit ,
                                         Status:String = "COMPLETE" ,
                                         aid:String = scala.util.Random.nextInt(1000).toString  ,
                                         aip:String = randomIp() ,
                                         cid:String = "1" ,
                                         event_platform:String = "mac" ,
                                         event_simpleName:String = "NetworkContainmentCompleted" ,
                                         id:String = scala.util.Random.nextInt(1000).toString  ,
                                         name:String = randomName ,
                                         timestamp:String =  generateTimestamp())





// COMMAND ----------

val gson = new com.google.gson.Gson
def getHostInforSampleJson(): String = {
   gson.toJson(new HostInfo)
}
