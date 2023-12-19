resource "datadog_monitor" "errorLogMonitor" {
    name = "Error Log Monitor"
    type = "log alert"
    query = "logs('error', index='main')"
    message = "Error log found"
    escalation_message = "Error log found"
    thresholds {
        critical = 1
    }
    notify_no_data = false
    renotify_interval = 60
    notify_audit = false
    timeout_h = 0
    notify_thresholds {
        critical = 1
    }
}