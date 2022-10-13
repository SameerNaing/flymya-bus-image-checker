from gql import gql


operators_query = gql(
    """
  query($filter: [filterInput], $first: Int!, $page: Int) {
    operators(
      filter: $filter
      first: $first
      page: $page
      orderBy: [{ field: "id", order: DESC }]
    ) {
      data {
        id
        code
        name
        product_type {
          id
          name
        }
      }
      paginatorInfo {
        count
        currentPage
        lastItem
        lastPage
        perPage
        total
        hasMorePages
      }
    }
  }
  """
)
