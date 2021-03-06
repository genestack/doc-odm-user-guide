require(shiny)

# TODO: autocomplete, existence
genes.input <- selectizeInput(
    inputId = 'gene.input',
    label = 'Genes',
    multiple = TRUE,
    choices = NULL
)

therapeutic.area.input <- selectInput(
    inputId = "therapeutic.area.input",
    label = "Therapeutic area",
    choices = NULL,
)

group.input <- selectInput(
    inputId = "group.input",
    label = "Group by",
    choices = c("Sex", "Disease", "Cell Type", "Smoking status"),
    selected = "Sex",
    multiple = FALSE
)

study.type.input <- selectInput(
    inputId = "study.type.input",
    label = "Study type",
    choices = c("Bulk Study", "Single-cell Study"),
    selected = "Bulk Study"
)

# TODO use choice names and values to distinguish study IDs vs names
GetStudiesCheckboxInput <- function(studies) {
    if (!is_empty(studies)) {
        checkboxGroupInput(
            inputId = "studies.checkbox.input",
            label = NULL,
            choiceNames = paste(studies[['genestack:accession']], studies[['Study Title']], sep=' '),
            choiceValues = studies[['genestack:accession']]
        )
    }
}

GetStudiesSelectAllInput <- function(studies) {
    if (!is_empty(studies)) {
        actionLink(
            inputId = "select.all",
            label = "Select All"
        )
    }
}

sample.filter.input <- textInput(
    inputId = "sample.filter.input",
    label = "Sample filter",
    value = NULL
)

expression.filter.input <- textInput(
    inputId = "expression.filter.input",
    label = "Expression filter",
    value = ""
)

variant.filter.input <- textInput(
  inputId = "variant.filter.input",
  label = "Variant filter",
  value = ""
)

SplitTextInput <- function(text.input) {
    unlist(lapply(strsplit(text.input, split = ",")[[1]], FUN = trimws))
}
