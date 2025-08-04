# JSON-Structure-Extract
A script that extracts the json structure of a JSON file. Useful when you need to provide the JSON structure to an LLM for analysis without exposing any sensitive data. Use with alias for speed. 

```bash
% jstruct -h
usage: json_structure_extract.py [-h] file

Inspect the structure of a JSON file.

positional arguments:
  file        Path to the JSON file

options:
  -h, --help  show this help message and exit
```

Example:
```bash
% jstruct crowdstrike_json_files/detects.json 
JSON Structure:
cid: str
created_timestamp: str
detection_id: str
device:
    device_id: str
    cid: str
    agent_load_flags: str
    agent_local_time: str
    agent_version: str
    config_id_base: str
    config_id_build: str
    config_id_platform: str
    external_ip: str
    hostname: str
    first_seen: str
    last_login_timestamp: str
    last_login_user: str
    last_seen: str
    local_ip: str
    mac_address: str
    machine_domain: str
    major_version: str
    minor_version: str
    os_version: str
    platform_id: str
    platform_name: str
    product_type_desc: str
    status: str
    system_manufacturer: str
    system_product_name: str
    tags:
        list:
            str
    groups:
        list:
            str
    modified_timestamp: str
behaviors:
    list:
        device_id: str
        timestamp: str
        behavior_id: str
        filename: str
        filepath: str
        alleged_filetype: str
        cmdline: str
        scenario: str
        objective: str
        tactic: str
        tactic_id: str
        technique: str
        technique_id: str
        display_name: str
        description: str
        severity: int
        confidence: int
        ioc_type: str
        ioc_value: str
        ioc_source: str
        ioc_description: str
        user_name: str
        user_id: str
        control_graph_id: str
        triggering_process_graph_id: str
        sha256: str
        md5: str
        parent_details:
            parent_sha256: str
            parent_md5: str
            parent_cmdline: str
            parent_process_graph_id: str
        pattern_disposition: int
        pattern_disposition_details:
            indicator: bool
            detect: bool
            inddet_mask: bool
            sensor_only: bool
            rooting: bool
            kill_process: bool
            kill_subprocess: bool
            quarantine_machine: bool
            quarantine_file: bool
            policy_disabled: bool
            kill_parent: bool
            operation_blocked: bool
            process_blocked: bool
            registry_operation_blocked: bool
            critical_process_disabled: bool
            bootup_safeguard_enabled: bool
            fs_operation_blocked: bool
            handle_operation_downgraded: bool
            kill_action_failed: bool
            blocking_unsupported_or_disabled: bool
            suspend_process: bool
            suspend_parent: bool
            response_action_already_applied: bool
            response_action_failed: bool
            mfa_required: bool
            response_action_triggered: bool
            prevention_provisioning_enabled: bool
            containment_file_system: bool
email_sent: bool
first_behavior: str
last_behavior: str
max_confidence: int
max_severity: int
max_severity_displayname: str
show_in_ui: bool
status: str
hostinfo:
    domain: str
seconds_to_triaged: int
seconds_to_resolved: int
behaviors_processed:
    list:
        str
date_updated: str
```
