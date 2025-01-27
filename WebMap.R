# libraries
library(ggraph)
library(igraph)
library(tidyverse)
library(collapsibleTree)

# Collapsible tree
df2 <- read_csv("C:/1 - Projects/WebMap/TestURLs.csv")

### Take each string in the first column, separate them out into individual columns
df2[1, 5:11] <- str_split_fixed(df2[1, 1], "/", n = 7)
df2[2, 5:11] <- str_split_fixed(df2[2, 1], "/", n = 7)
df2[3, 5:11] <- str_split_fixed(df2[3, 1], "/", n = 7)
df2[4, 5:11] <- str_split_fixed(df2[4, 1], "/", n = 7)
df2[5, 5:11] <- str_split_fixed(df2[5, 1], "/", n = 7)
df2[6, 5:11] <- str_split_fixed(df2[6, 1], "/", n = 7)
df2[7, 5:11] <- str_split_fixed(df2[7, 1], "/", n = 7)
df2[8, 5:11] <- str_split_fixed(df2[8, 1], "/", n = 7)
df2[9, 5:11] <- str_split_fixed(df2[9, 1], "/", n = 7)
df2[10, 5:11] <- str_split_fixed(df2[10, 1], "/", n = 7)
df2[11, 5:11] <- str_split_fixed(df2[11, 1], "/", n = 7)

tree <- collapsibleTree(
  df2, 
  c("V1", "V2", "V3", "V4", "V5", "V6"), 
  attribute = "leafCount",
  fontSize = 20, 
  nodeSize = "pageviews", 
  collapsed = FALSE,
  tooltip = TRUE,
  tooltipHtml = author
  )

tree

# Create root column with NA values
df2 <- mutate(df2, V0 = NA)

# Collapsible Tree Network
df2$Color <- df2$

levels(df2$Color) <- colorspace::rainbow_hcl(11)

collapsibleTreeNetwork(
  df2,
  attribute = "pageviews",
  fill = "Color",
  nodeSize = "pageviews",
  collapsed = FALSE
)

tree

# Create a function that will take each row 
