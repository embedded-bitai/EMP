import React, { useState } from 'react';
import clsx from 'clsx';
import PropTypes from 'prop-types';
import { v4 as uuid } from 'uuid';
import moment from 'moment';
import {
  Box,
  Button,
  Card,
  CardHeader,
  Divider,
  IconButton,
  List,
  ListItem,
  ListItemAvatar,
  ListItemText,
  makeStyles
} from '@material-ui/core';
import MoreVertIcon from '@material-ui/icons/MoreVert';
import ArrowRightIcon from '@material-ui/icons/ArrowRight';

const data = [
  {
    id: uuid(),
    name: '푸름 당베르',
    imageUrl: '/static/images/products/cheese_1.jpg',
    updatedAt: moment().subtract(2, 'hours')
  },
  {
    id: uuid(),
    name: '블루치즈 크림치즈',
    imageUrl: '/static/images/products/cheese_2.jpg',
    updatedAt: moment().subtract(2, 'hours')
  },
  {
    id: uuid(),
    name: '저지 고다 머추어 치즈',
    imageUrl: '/static/images/products/cheese_3.jpg',
    updatedAt: moment().subtract(3, 'hours')
  },
  {
    id: uuid(),
    name: '마스카포네 치즈',
    imageUrl: '/static/images/products/cheese_4.jpg',
    updatedAt: moment().subtract(5, 'hours')
  },
  {
    id: uuid(),
    name: '부라타 치즈',
    imageUrl: '/static/images/products/cheese_5.jpg',
    updatedAt: moment().subtract(9, 'hours')
  }
];

const useStyles = makeStyles(({
  root: {
    height: '100%'
  },
  image: {
    height: 48,
    width: 48
  }
}));

const LatestProducts = () => {
  const classes = useStyles();
  const [products] = useState(data);

  return (
    <Card>
      <CardHeader
        subtitle={`${products.length} in total`}
        title="Latest Products"
      />
      <Divider />
      <List>
        {products.map((product, i) => (
          <ListItem
            divider={i < products.length - 1}
            key={product.id}
          >
            <ListItemAvatar>
              <img
                alt="Product"
                className={classes.image}
                src={product.imageUrl}
              />
            </ListItemAvatar>
            <ListItemText
              primary={product.name}
              secondary={`Updated ${product.updatedAt.fromNow()}`}
            />
            <IconButton
              edge="end"
              size="small"
            >
              <MoreVertIcon />
            </IconButton>
          </ListItem>
        ))}
      </List>
      <Divider />
      <Box
        display="flex"
        justifyContent="flex-end"
        p={2}
      >
        <Button
          color="primary"
          endIcon={<ArrowRightIcon />}
          size="small"
          variant="text"
        >
          View all
        </Button>
      </Box>
    </Card>
  );
};

LatestProducts.propTypes = {
  className: PropTypes.string
};

export default LatestProducts;
