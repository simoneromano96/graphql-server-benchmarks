# graphql-server-benchmarks

A set of graphql server/library implementation benchmarks

## Libraries requirements

MUST means that the library implements the feature.

SHOULD means that the library can implement the feature.

* Must implement the core GraphQL specification (including subscriptions)
* Must be mantained
* Must implement dataloader
* Should implement GraphQL extensions (ex. `multipart`, `federation`, `pagination`)
* If not implemented the library's name appears like **this**
* Should use code-first approach
  * If not implemented the library's name appears like *this*

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
  * Only implements core features, can't find file-upload or federation

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

* *graphql-dotnet*
* 
* hotchocolate
* EntityGraphQL
* NGraphQL

### Ruby

* graphql-ruby

* agoo

### Rust

* graphql-rust/juniper 

* async-graphql/async-graphql

### Elixir

* absinthe

* graphql-elixir/graphql

### Scala

* sangria-graphql/sangria

* ghostdogpr/caliban 

### Haskell

* morpheus-graphql

* mu-haskell

