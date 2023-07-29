"use client";

import { Typography } from "@mui/material";

interface TestListItemProps {
  title: string;
}

const TestListItem = ({ title }: TestListItemProps) => {
  const handleClick = () => {
    console.log(`Clicked ${title}`);
  };

  return (
    <Typography variant="h6" onClick={handleClick}>
      {title}
    </Typography>
  );
};

export default TestListItem;
