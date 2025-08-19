```mermaid
classDiagram
    %% --- Association ---
    Module --> Event : creates

    %% --- Aggregation ---
    Storage o-- Product : store


    %% --- Composition ---
    Header *-- Logo
    Header *-- NavBar
    Header *-- Login
    
```