# graphql-server-benchmarks

A set of graphql server/library implementation benchmarks

## Libraries requirements

MUST means that the library implements the feature.

SHOULD means that the library can implement the feature.

* Must implement the core GraphQL specification (including subscriptions)
* Must be mantained
* Must implement dataloader
* Should implement GraphQL extensions (ex. `multipart`, `federation`, `pagination (relay)`)
  * While they are extensions of the standard, they are useful and should be considered when choosing a library, the least important one for me is `federation` because we can use "plain olde" schema stitching which works well
  * If not implemented the library's name appears like **this**
* Should use code-first / struct-first approach
  * If not implemented the library's name appears like *this*

Note that the above requirements list is mostly from personal preference, I prefer code-first, I prefer having the extensions available.

## Library list

### Node

#### Server

* mercurius

* apollo

* express-graphql

#### Library

* nexus

* typegraphql

### GoLang

* *99designs/gqlgen*
  * https://github.com/99designs/gqlgen/blob/master/docs/content/reference/file-upload.md
  * https://github.com/99designs/gqlgen/blob/master/example/starwars/schema.graphql
  * https://gqlgen.com/recipes/federation/
* **ccbrown/api-fu**
  * ???

### PHP

* **API Platform**
  * https://api-platform.com/docs/core/graphql/#handling-file-upload
  * https://api-platform.com/docs/core/graphql/#using-the-cursor-based-pagination
  * No federation
* ***Lighthouse***
  * https://lighthouse-php.com/5.3/digging-deeper/file-uploads.html
  * https://lighthouse-php.com/master/digging-deeper/relay.html
  * No federation
* *Siler*
  * https://github.com/leocavalcante/siler/tree/main/examples/graphql
  * ???

### Python

* graphql-python/graphene
  * https://docs.graphene-python.org/en/latest/relay/
  * https://github.com/lmcgartland/graphene-file-upload
  * https://pypi.org/project/graphene-federation/
* *mirumee/ariadne*
  * https://ariadnegraphql.org/docs/file-uploads
  * https://ariadnegraphql.org/docs/apollo-federation
  * https://github.com/mirumee/ariadne/issues/188 (?)
* strawberry-graphql/strawberry
  * Missing docs for the additional features, should be included
* ***tartiflette/tartiflette***
  * https://tartiflette.io/docs/tutorial/getting-started

### Java

* ***graphql-java*** 
  * https://www.graphql-java.com/documentation/v16/relay/
  * Federation unsopported (https://github.com/rkudryashov/graphql-java-federation)
  * File upload is hacky (https://stackoverflow.com/questions/57372259/how-to-upload-files-with-graphql-java)

### Kotlin

* **graphql-kotlin**
  * https://expediagroup.github.io/graphql-kotlin/docs/schema-generator/federation/apollo-federation
  * Relay can be obtained manually
  * File upload is hacky (https://github.com/ExpediaGroup/graphql-kotlin/issues/1036)

### .NET C#

* **graphql-dotnet**
  * No federation
  * https://graphql-dotnet.github.io/docs/getting-started/relay
  * https://github.com/JannikLassahn/graphql-dotnet-upload
* **hotchocolate**
  * No federation, provides alternative schema stitching (not sure if I should count it)
  * https://chillicream.com/docs/hotchocolate/v10/schema/relay/
  * Upload is a WIP: https://github.com/ChilliCream/hotchocolate/pull/2936

### Rust

* **graphql-rust/juniper**
  * No federation
  * No relay
  * No file upload
* async-graphql/async-graphql
  * https://async-graphql.github.io/async-graphql/en/apollo_federation.html
  * https://async-graphql.github.io/async-graphql/en/cursor_connections.html
  * https://github.com/async-graphql/examples/blob/master/actix-web/upload/src/main.rs

### Elixir

* absinthe
  * No federation
  * https://hexdocs.pm/absinthe/relay.html
  * https://hexdocs.pm/absinthe/file-uploads.html#example

### Scala

* **sangria-graphql/sangria**
  * No federation https://github.com/sangria-graphql/sangria/issues/462
  * https://github.com/sangria-graphql/sangria-relay
  * No file upload https://github.com/sangria-graphql/sangria/issues/503
* ghostdogpr/caliban 
  * https://ghostdogpr.github.io/caliban/docs/federation.html
  * Relay (implemented "manually") https://github.com/ghostdogpr/caliban/issues/132
  * https://github.com/ghostdogpr/caliban/blob/master/adapters/play/src/main/scala/caliban/uploads/Upload.scala

### Haskell

* **morpheus-graphql**
  * No federation
  * No relay
  * No uploads
* *mu-haskell*
  * No federation
  * No relay
  * No uploads

