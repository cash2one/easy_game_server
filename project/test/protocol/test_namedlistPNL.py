import sys
sys.path.append('../autotest_lib')
from namedlist_Generator_lib_easy import *
SLoadFinishedReq = namedList("SLoadFinishedReq", "intoScene,")
SCreateReq = namedList("SCreateReq", "rolename[64],professionId,")
SCreateExReq = namedList("SCreateExReq", "rolename[64],professionId,vip,")
SLogoffReq = namedList("SLogoffReq", "")
SLogoffRsp = namedList("SLogoffRsp", "")
SRegisterReq = namedList("SRegisterReq", "account[32],pwd[32],mac[32],")
SRegisterRsp = namedList("SRegisterRsp", "errcode,")
SKickNtf = namedList("SKickNtf", "")
SEasyLoginReq = namedList("SEasyLoginReq", "type,easyAccount[128],")
SBasicRoleInfo = namedList("SBasicRoleInfo", "userid,guid,showLevel,mateid,macAddress[20],rolename[64],level,professionId,exp,popularity,expTotal,diamond,money,exploit,vigor,vigorMax,leaderForce,killingValue,halliconId,")
SRoleParameters = namedList("SRoleParameters", "quizCount,quizScore,moral,tidy,")
SRole = namedList("SRole", "roleBasic=SBasicRoleInfo,paraNow=SRoleParameters,")
SEasyRoleInfo4Login = namedList("SEasyRoleInfo4Login", "rolename[32],userid,")
SEasyRoleInfo4LoginList = namedList("SEasyRoleInfo4LoginList", "count,easyRoleList=SEasyRoleInfo4Login[5],")
SEasyLoginRsp = namedList("SEasyLoginRsp", "type,errcode,roleList=SEasyRoleInfo4LoginList,")
SEnterReq = namedList("SEnterReq", "userid,")
SEnterRsp = namedList("SEnterRsp", "errcode,roleCount,roles=SRole[1],")
SBindAccountReq = namedList("SBindAccountReq", "account[32],pwd[32],")
SBindAccountRsp = namedList("SBindAccountRsp", "errcode,")
SCreateRsp = namedList("SCreateRsp", "errcode,name[32],userid,")
SBasicData = namedList("SBasicData", "t,v,")
SBasicDataString = namedList("SBasicDataString", "t,sv[32],")
SBasicDataStringNtf = namedList("SBasicDataStringNtf", "count,t=SBasicDataString[32],")
SBasicDataNtf = namedList("SBasicDataNtf", "count,t=SBasicData[32],")
SBasicDataEx = namedList("SBasicDataEx", "guid,ns=SBasicDataNtf,")
SBasicDataExNtf = namedList("SBasicDataExNtf", "count,updates=SBasicDataEx[21],")
SBasicDataChangeReq = namedList("SBasicDataChangeReq", "sbdn=SBasicDataNtf,")
SBasicDataChangeNtf = namedList("SBasicDataChangeNtf", "sbdn=SBasicDataNtf,")
SBasicDataStringChangeReq = namedList("SBasicDataStringChangeReq", "sbdn=SBasicDataStringNtf,")
SBasicDataStringChangeNtf = namedList("SBasicDataStringChangeNtf", "sbdn=SBasicDataStringNtf,")
SGlobalNtf = namedList("SGlobalNtf", "t,msg[512],role[64],")
SBasicDataBroadcastNtf = namedList("SBasicDataBroadcastNtf", "guid,t,v,jerseyId,")
SProtocolVersionNtf = namedList("SProtocolVersionNtf", "v,")
SProtocolTypeRpt = namedList("SProtocolTypeRpt", "type,version,")
SProtocolTypeRsp = namedList("SProtocolTypeRsp", "errcode,")
SGmcmdReq = namedList("SGmcmdReq", "cmd[64],")
SGmcmdRsp = namedList("SGmcmdRsp", "nouse,")
SProbeNtf = namedList("SProbeNtf", "a,b,c,d,")
SProbeAnswer = namedList("SProbeAnswer", "a,b,c,d,")
SLeaveMsg2GMReq = namedList("SLeaveMsg2GMReq", "msg[256],")
SGMAnswerRsp = namedList("SGMAnswerRsp", "answer[256],")
SServerLoadFinishNtf = namedList("SServerLoadFinishNtf", "temp,")
SStageInfo = namedList("SStageInfo", "stageId,md5[32],name[64],desc[256],size,")
SStageFile = namedList("SStageFile", "stageId,blockId,nextBlcokId,length,file[20480],")
SGetAllStageDescReq = namedList("SGetAllStageDescReq", "")
SGetAllStageDescRsp = namedList("SGetAllStageDescRsp", "count,stages=SStageInfo[50],")
SGetStageReq = namedList("SGetStageReq", "stageId,blockId,")
SGetStageRsp = namedList("SGetStageRsp", "totalSize,file=SStageFile,")
STreasure = namedList("STreasure", "guid,count,itemId,createTime,")
STreasureInBag = namedList("STreasureInBag", "index,t=STreasure,leftTimeSecond,")
STreasureUpdateNtf = namedList("STreasureUpdateNtf", "count,treasures=STreasureInBag[100],")
SGeneralErrorNtf = namedList("SGeneralErrorNtf", "errcode,msg[512],")
SGeneralWordsNtf = namedList("SGeneralWordsNtf", "msg[512],")
SServerStatusReporter = namedList("SServerStatusReporter", "servername[64],maxLoad,currentLoad,protocolVer,")
SLogConsumeDiamond = namedList("SLogConsumeDiamond", "type,gID,itemID,")
SPackedFileIndex = namedList("SPackedFileIndex", "name[128],startIndex,endIndex,")
SPackedFiles = namedList("SPackedFiles", "count,files=SPackedFileIndex[100],")
SMiscDB = namedList("SMiscDB", "shootMonsterCount,")
SGetRoleInfoReq = namedList("SGetRoleInfoReq", "i,")
SGetRoleInfoRsp = namedList("SGetRoleInfoRsp", "role=SRole,")
