export interface ValidationResult {
  severity: 'violation' | 'warning' | 'info'
  focus_node: string
  result_path: string
  message: string
}

export interface ValidationReport {
  conforms: boolean
  results: ValidationResult[]
  results_text: string
}
