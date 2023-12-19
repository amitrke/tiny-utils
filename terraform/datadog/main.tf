resource "datadog_monitor" "errorLogMonitor" {
    name = "Error Log Monitor"
    type = "log alert"
    query = "count_over_time(logs('error').index('main').overAll().last('5m')) > 0"  # Adjust the time frame as needed
    message = "Error log found"
    escalation_message = "Error log found"
    monitor_thresholds {
        critical = 1
    }
    notify_no_data = false
    renotify_interval = 60
    notify_audit = false
    timeout_h = 0
}
