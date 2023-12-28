# @generated

# This file was generated by running `python -m dagster._grpc.compile`
# Do not edit this file directly, and do not attempt to recompile it using
# grpc_tools.protoc directly, as several changes must be made to the raw output

# noqa: SLF001

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\tapi.proto\x12\x03\x61pi"\x07\n\x05\x45mpty"\x1b\n\x0bPingRequest\x12\x0c\n\x04\x65\x63ho\x18\x01 \x01(\t"D\n\tPingReply\x12\x0c\n\x04\x65\x63ho\x18\x01 \x01(\t\x12)\n!serialized_server_health_metadata\x18\x02 \x01(\t"=\n\x14StreamingPingRequest\x12\x17\n\x0fsequence_length\x18\x01 \x01(\x05\x12\x0c\n\x04\x65\x63ho\x18\x02 \x01(\t";\n\x12StreamingPingEvent\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\x12\x0c\n\x04\x65\x63ho\x18\x02 \x01(\t"%\n\x10GetServerIdReply\x12\x11\n\tserver_id\x18\x01 \x01(\t"O\n\x1c\x45xecutionPlanSnapshotRequest\x12/\n\'serialized_execution_plan_snapshot_args\x18\x01 \x01(\t"H\n\x1a\x45xecutionPlanSnapshotReply\x12*\n"serialized_execution_plan_snapshot\x18\x01 \x01(\t"H\n\x1d\x45xternalPartitionNamesRequest\x12\'\n\x1fserialized_partition_names_args\x18\x01 \x01(\t"p\n\x1b\x45xternalPartitionNamesReply\x12Q\nIserialized_external_partition_names_or_external_partition_execution_error\x18\x01 \x01(\t"4\n\x1b\x45xternalNotebookDataRequest\x12\x15\n\rnotebook_path\x18\x01 \x01(\t",\n\x19\x45xternalNotebookDataReply\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c"C\n\x1e\x45xternalPartitionConfigRequest\x12!\n\x19serialized_partition_args\x18\x01 \x01(\t"r\n\x1c\x45xternalPartitionConfigReply\x12R\nJserialized_external_partition_config_or_external_partition_execution_error\x18\x01 \x01(\t"A\n\x1c\x45xternalPartitionTagsRequest\x12!\n\x19serialized_partition_args\x18\x01 \x01(\t"n\n\x1a\x45xternalPartitionTagsReply\x12P\nHserialized_external_partition_tags_or_external_partition_execution_error\x18\x01 \x01(\t"c\n*ExternalPartitionSetExecutionParamsRequest\x12\x35\n-serialized_partition_set_execution_param_args\x18\x01 \x01(\t"\x19\n\x17ListRepositoriesRequest"O\n\x15ListRepositoriesReply\x12\x36\n.serialized_list_repositories_response_or_error\x18\x01 \x01(\t"Y\n%ExternalPipelineSubsetSnapshotRequest\x12\x30\n(serialized_pipeline_subset_snapshot_args\x18\x01 \x01(\t"Y\n#ExternalPipelineSubsetSnapshotReply\x12\x32\n*serialized_external_pipeline_subset_result\x18\x01 \x01(\t"a\n\x19\x45xternalRepositoryRequest\x12+\n#serialized_repository_python_origin\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x65\x66\x65r_snapshots\x18\x02 \x01(\x08"F\n\x17\x45xternalRepositoryReply\x12+\n#serialized_external_repository_data\x18\x01 \x01(\t"i\n StreamingExternalRepositoryEvent\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\x12,\n$serialized_external_repository_chunk\x18\x02 \x01(\t"W\n ExternalScheduleExecutionRequest\x12\x33\n+serialized_external_schedule_execution_args\x18\x01 \x01(\t"S\n\x1e\x45xternalSensorExecutionRequest\x12\x31\n)serialized_external_sensor_execution_args\x18\x01 \x01(\t"H\n\x13StreamingChunkEvent\x12\x17\n\x0fsequence_number\x18\x01 \x01(\x05\x12\x18\n\x10serialized_chunk\x18\x02 \x01(\t"@\n\x13ShutdownServerReply\x12)\n!serialized_shutdown_server_result\x18\x01 \x01(\t"E\n\x16\x43\x61ncelExecutionRequest\x12+\n#serialized_cancel_execution_request\x18\x01 \x01(\t"B\n\x14\x43\x61ncelExecutionReply\x12*\n"serialized_cancel_execution_result\x18\x01 \x01(\t"L\n\x19\x43\x61nCancelExecutionRequest\x12/\n\'serialized_can_cancel_execution_request\x18\x01 \x01(\t"I\n\x17\x43\x61nCancelExecutionReply\x12.\n&serialized_can_cancel_execution_result\x18\x01 \x01(\t"6\n\x0fStartRunRequest\x12#\n\x1bserialized_execute_run_args\x18\x01 \x01(\t"4\n\rStartRunReply\x12#\n\x1bserialized_start_run_result\x18\x01 \x01(\t"8\n\x14GetCurrentImageReply\x12 \n\x18serialized_current_image\x18\x01 \x01(\t"6\n\x13GetCurrentRunsReply\x12\x1f\n\x17serialized_current_runs\x18\x01 \x01(\t"L\n\x12\x45xternalJobRequest\x12$\n\x1cserialized_repository_origin\x18\x01 \x01(\t\x12\x10\n\x08job_name\x18\x02 \x01(\t"I\n\x10\x45xternalJobReply\x12\x1b\n\x13serialized_job_data\x18\x01 \x01(\t\x12\x18\n\x10serialized_error\x18\x02 \x01(\t"D\n\x1e\x45xternalScheduleExecutionReply\x12"\n\x1aserialized_schedule_result\x18\x01 \x01(\t"@\n\x1c\x45xternalSensorExecutionReply\x12 \n\x18serialized_sensor_result\x18\x01 \x01(\t"\x13\n\x11ReloadCodeRequest"+\n\x0fReloadCodeReply\x12\x18\n\x10serialized_error\x18\x02 \x01(\t2\xe9\x10\n\nDagsterApi\x12*\n\x04Ping\x12\x10.api.PingRequest\x1a\x0e.api.PingReply"\x00\x12/\n\tHeartbeat\x12\x10.api.PingRequest\x1a\x0e.api.PingReply"\x00\x12G\n\rStreamingPing\x12\x19.api.StreamingPingRequest\x1a\x17.api.StreamingPingEvent"\x00\x30\x01\x12\x32\n\x0bGetServerId\x12\n.api.Empty\x1a\x15.api.GetServerIdReply"\x00\x12]\n\x15\x45xecutionPlanSnapshot\x12!.api.ExecutionPlanSnapshotRequest\x1a\x1f.api.ExecutionPlanSnapshotReply"\x00\x12N\n\x10ListRepositories\x12\x1c.api.ListRepositoriesRequest\x1a\x1a.api.ListRepositoriesReply"\x00\x12`\n\x16\x45xternalPartitionNames\x12".api.ExternalPartitionNamesRequest\x1a .api.ExternalPartitionNamesReply"\x00\x12Z\n\x14\x45xternalNotebookData\x12 .api.ExternalNotebookDataRequest\x1a\x1e.api.ExternalNotebookDataReply"\x00\x12\x63\n\x17\x45xternalPartitionConfig\x12#.api.ExternalPartitionConfigRequest\x1a!.api.ExternalPartitionConfigReply"\x00\x12]\n\x15\x45xternalPartitionTags\x12!.api.ExternalPartitionTagsRequest\x1a\x1f.api.ExternalPartitionTagsReply"\x00\x12t\n#ExternalPartitionSetExecutionParams\x12/.api.ExternalPartitionSetExecutionParamsRequest\x1a\x18.api.StreamingChunkEvent"\x00\x30\x01\x12x\n\x1e\x45xternalPipelineSubsetSnapshot\x12*.api.ExternalPipelineSubsetSnapshotRequest\x1a(.api.ExternalPipelineSubsetSnapshotReply"\x00\x12T\n\x12\x45xternalRepository\x12\x1e.api.ExternalRepositoryRequest\x1a\x1c.api.ExternalRepositoryReply"\x00\x12?\n\x0b\x45xternalJob\x12\x17.api.ExternalJobRequest\x1a\x15.api.ExternalJobReply"\x00\x12h\n\x1bStreamingExternalRepository\x12\x1e.api.ExternalRepositoryRequest\x1a%.api.StreamingExternalRepositoryEvent"\x00\x30\x01\x12`\n\x19\x45xternalScheduleExecution\x12%.api.ExternalScheduleExecutionRequest\x1a\x18.api.StreamingChunkEvent"\x00\x30\x01\x12m\n\x1dSyncExternalScheduleExecution\x12%.api.ExternalScheduleExecutionRequest\x1a#.api.ExternalScheduleExecutionReply"\x00\x12\\\n\x17\x45xternalSensorExecution\x12#.api.ExternalSensorExecutionRequest\x1a\x18.api.StreamingChunkEvent"\x00\x30\x01\x12g\n\x1bSyncExternalSensorExecution\x12#.api.ExternalSensorExecutionRequest\x1a!.api.ExternalSensorExecutionReply"\x00\x12\x38\n\x0eShutdownServer\x12\n.api.Empty\x1a\x18.api.ShutdownServerReply"\x00\x12K\n\x0f\x43\x61ncelExecution\x12\x1b.api.CancelExecutionRequest\x1a\x19.api.CancelExecutionReply"\x00\x12T\n\x12\x43\x61nCancelExecution\x12\x1e.api.CanCancelExecutionRequest\x1a\x1c.api.CanCancelExecutionReply"\x00\x12\x36\n\x08StartRun\x12\x14.api.StartRunRequest\x1a\x12.api.StartRunReply"\x00\x12:\n\x0fGetCurrentImage\x12\n.api.Empty\x1a\x19.api.GetCurrentImageReply"\x00\x12\x38\n\x0eGetCurrentRuns\x12\n.api.Empty\x1a\x18.api.GetCurrentRunsReply"\x00\x12<\n\nReloadCode\x12\x16.api.ReloadCodeRequest\x1a\x14.api.ReloadCodeReply"\x00\x62\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "api_pb2", _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals["_EMPTY"]._serialized_start = 18
    _globals["_EMPTY"]._serialized_end = 25
    _globals["_PINGREQUEST"]._serialized_start = 27
    _globals["_PINGREQUEST"]._serialized_end = 54
    _globals["_PINGREPLY"]._serialized_start = 56
    _globals["_PINGREPLY"]._serialized_end = 124
    _globals["_STREAMINGPINGREQUEST"]._serialized_start = 126
    _globals["_STREAMINGPINGREQUEST"]._serialized_end = 187
    _globals["_STREAMINGPINGEVENT"]._serialized_start = 189
    _globals["_STREAMINGPINGEVENT"]._serialized_end = 248
    _globals["_GETSERVERIDREPLY"]._serialized_start = 250
    _globals["_GETSERVERIDREPLY"]._serialized_end = 287
    _globals["_EXECUTIONPLANSNAPSHOTREQUEST"]._serialized_start = 289
    _globals["_EXECUTIONPLANSNAPSHOTREQUEST"]._serialized_end = 368
    _globals["_EXECUTIONPLANSNAPSHOTREPLY"]._serialized_start = 370
    _globals["_EXECUTIONPLANSNAPSHOTREPLY"]._serialized_end = 442
    _globals["_EXTERNALPARTITIONNAMESREQUEST"]._serialized_start = 444
    _globals["_EXTERNALPARTITIONNAMESREQUEST"]._serialized_end = 516
    _globals["_EXTERNALPARTITIONNAMESREPLY"]._serialized_start = 518
    _globals["_EXTERNALPARTITIONNAMESREPLY"]._serialized_end = 630
    _globals["_EXTERNALNOTEBOOKDATAREQUEST"]._serialized_start = 632
    _globals["_EXTERNALNOTEBOOKDATAREQUEST"]._serialized_end = 684
    _globals["_EXTERNALNOTEBOOKDATAREPLY"]._serialized_start = 686
    _globals["_EXTERNALNOTEBOOKDATAREPLY"]._serialized_end = 730
    _globals["_EXTERNALPARTITIONCONFIGREQUEST"]._serialized_start = 732
    _globals["_EXTERNALPARTITIONCONFIGREQUEST"]._serialized_end = 799
    _globals["_EXTERNALPARTITIONCONFIGREPLY"]._serialized_start = 801
    _globals["_EXTERNALPARTITIONCONFIGREPLY"]._serialized_end = 915
    _globals["_EXTERNALPARTITIONTAGSREQUEST"]._serialized_start = 917
    _globals["_EXTERNALPARTITIONTAGSREQUEST"]._serialized_end = 982
    _globals["_EXTERNALPARTITIONTAGSREPLY"]._serialized_start = 984
    _globals["_EXTERNALPARTITIONTAGSREPLY"]._serialized_end = 1094
    _globals["_EXTERNALPARTITIONSETEXECUTIONPARAMSREQUEST"]._serialized_start = 1096
    _globals["_EXTERNALPARTITIONSETEXECUTIONPARAMSREQUEST"]._serialized_end = 1195
    _globals["_LISTREPOSITORIESREQUEST"]._serialized_start = 1197
    _globals["_LISTREPOSITORIESREQUEST"]._serialized_end = 1222
    _globals["_LISTREPOSITORIESREPLY"]._serialized_start = 1224
    _globals["_LISTREPOSITORIESREPLY"]._serialized_end = 1303
    _globals["_EXTERNALPIPELINESUBSETSNAPSHOTREQUEST"]._serialized_start = 1305
    _globals["_EXTERNALPIPELINESUBSETSNAPSHOTREQUEST"]._serialized_end = 1394
    _globals["_EXTERNALPIPELINESUBSETSNAPSHOTREPLY"]._serialized_start = 1396
    _globals["_EXTERNALPIPELINESUBSETSNAPSHOTREPLY"]._serialized_end = 1485
    _globals["_EXTERNALREPOSITORYREQUEST"]._serialized_start = 1487
    _globals["_EXTERNALREPOSITORYREQUEST"]._serialized_end = 1584
    _globals["_EXTERNALREPOSITORYREPLY"]._serialized_start = 1586
    _globals["_EXTERNALREPOSITORYREPLY"]._serialized_end = 1656
    _globals["_STREAMINGEXTERNALREPOSITORYEVENT"]._serialized_start = 1658
    _globals["_STREAMINGEXTERNALREPOSITORYEVENT"]._serialized_end = 1763
    _globals["_EXTERNALSCHEDULEEXECUTIONREQUEST"]._serialized_start = 1765
    _globals["_EXTERNALSCHEDULEEXECUTIONREQUEST"]._serialized_end = 1852
    _globals["_EXTERNALSENSOREXECUTIONREQUEST"]._serialized_start = 1854
    _globals["_EXTERNALSENSOREXECUTIONREQUEST"]._serialized_end = 1937
    _globals["_STREAMINGCHUNKEVENT"]._serialized_start = 1939
    _globals["_STREAMINGCHUNKEVENT"]._serialized_end = 2011
    _globals["_SHUTDOWNSERVERREPLY"]._serialized_start = 2013
    _globals["_SHUTDOWNSERVERREPLY"]._serialized_end = 2077
    _globals["_CANCELEXECUTIONREQUEST"]._serialized_start = 2079
    _globals["_CANCELEXECUTIONREQUEST"]._serialized_end = 2148
    _globals["_CANCELEXECUTIONREPLY"]._serialized_start = 2150
    _globals["_CANCELEXECUTIONREPLY"]._serialized_end = 2216
    _globals["_CANCANCELEXECUTIONREQUEST"]._serialized_start = 2218
    _globals["_CANCANCELEXECUTIONREQUEST"]._serialized_end = 2294
    _globals["_CANCANCELEXECUTIONREPLY"]._serialized_start = 2296
    _globals["_CANCANCELEXECUTIONREPLY"]._serialized_end = 2369
    _globals["_STARTRUNREQUEST"]._serialized_start = 2371
    _globals["_STARTRUNREQUEST"]._serialized_end = 2425
    _globals["_STARTRUNREPLY"]._serialized_start = 2427
    _globals["_STARTRUNREPLY"]._serialized_end = 2479
    _globals["_GETCURRENTIMAGEREPLY"]._serialized_start = 2481
    _globals["_GETCURRENTIMAGEREPLY"]._serialized_end = 2537
    _globals["_GETCURRENTRUNSREPLY"]._serialized_start = 2539
    _globals["_GETCURRENTRUNSREPLY"]._serialized_end = 2593
    _globals["_EXTERNALJOBREQUEST"]._serialized_start = 2595
    _globals["_EXTERNALJOBREQUEST"]._serialized_end = 2671
    _globals["_EXTERNALJOBREPLY"]._serialized_start = 2673
    _globals["_EXTERNALJOBREPLY"]._serialized_end = 2746
    _globals["_EXTERNALSCHEDULEEXECUTIONREPLY"]._serialized_start = 2748
    _globals["_EXTERNALSCHEDULEEXECUTIONREPLY"]._serialized_end = 2816
    _globals["_EXTERNALSENSOREXECUTIONREPLY"]._serialized_start = 2818
    _globals["_EXTERNALSENSOREXECUTIONREPLY"]._serialized_end = 2882
    _globals["_RELOADCODEREQUEST"]._serialized_start = 2884
    _globals["_RELOADCODEREQUEST"]._serialized_end = 2903
    _globals["_RELOADCODEREPLY"]._serialized_start = 2905
    _globals["_RELOADCODEREPLY"]._serialized_end = 2948
    _globals["_DAGSTERAPI"]._serialized_start = 2951
    _globals["_DAGSTERAPI"]._serialized_end = 5104
# @@protoc_insertion_point(module_scope)
