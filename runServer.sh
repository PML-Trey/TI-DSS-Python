#!/bin/bash

#Change to point to the ccs_base directory on your machine
ccs_base_dir=".../ti/ccs1020/ccs/ccs_base"

dss_jar="${ccs_base_dir}/DebugServer/packages/ti/dss/java/dss.jar"
environment_jar="${ccs_base_dir}/DebugServer/packages/ti/dss/java/com.ti.ccstudio.scripting.environment_3.1.0.jar"
debug_engine_jar="${ccs_base_dir}/DebugServer/packages/ti/dss/java/com.ti.debug.engine_1.0.0.jar"
java_dir="/home/trey/ti/ccs1020/ccs/eclipse/jre"

export CLASSPATH=${CLASSPATH}:${dss_jar}:${environment_jar}:${debug_engine_jar}
#printenv CLASSPATH

jython TI-DSS-Python-Server.jy

