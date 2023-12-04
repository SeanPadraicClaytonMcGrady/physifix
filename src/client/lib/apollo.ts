import { ApolloClient, InMemoryCache, HttpLink } from "@apollo/client";

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/", // Replace with your Django GraphQL endpoint
  cache: new InMemoryCache(),
});

export default client;
