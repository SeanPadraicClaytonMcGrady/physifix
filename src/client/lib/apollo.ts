import { ApolloClient, InMemoryCache } from "@apollo/client";

const client = new ApolloClient({
  uri: "http://localhost:8000/graphene/", // Replace with your Django GraphQL endpoint
  cache: new InMemoryCache(),
});

export default client;
