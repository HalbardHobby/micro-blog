import React from 'react';

export default ({ comments }) => {
  
  const renderedComments = comments.map(comment => {
    let content = comment.content

    if (comment.status === "pending") {
      content = "This comment is awaiting moderation."
    }
    else if (comment.status === "rejected") {
      content = "This commment has been rejected."
    }

    return <li key={comment.id}>{content}</li>
  })

  return <ul>
    {renderedComments}
  </ul>
}