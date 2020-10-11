import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import {
  Avatar,
  Box,
  Card,
  CardContent,
  Divider,
  Grid,
  Typography,
  makeStyles
} from '@material-ui/core';
import AccessTimeIcon from '@material-ui/icons/AccessTime';
import GetAppIcon from '@material-ui/icons/GetApp';

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexDirection: 'column'
  },
  statsItem: {
    alignItems: 'center',
    display: 'flex'
  },
  statsIcon: {
    marginRight: theme.spacing(1)
  }
}));

const ProductCard = () => {
  const classes = useStyles();

  return (
    <Card>

      <CardContent>

        <Box
          display="flex"
          justifyContent="center"
          mb={3}
        >
          <Avatar
            src="/static/images/products/cheese_2.jpg"
            variant="circle"
          />
        </Box>

        <Typography
          align="center"
          color="textPrimary"
          gutterBottom
          variant="h5"
        >
        <h5>치즈 추천 플랫폼 'OOO' 입니다.</h5>
        </Typography>

        <Typography
          align="center"
          color="textPrimary"
          variant="body1"
        >
        <h2>치즈 주문과 판매, 챗봇 상담을 통해</h2>
        <h2>사용자 맞춤 치즈 추천 서비스를 제공합니다.</h2>
        </Typography>
      </CardContent>

      <Box flexGrow={1} />
      <Divider />
      <Box p={2}>
        <Grid
          container
          justify="space-between"
          spacing={2}
        >
          <Grid
            className={classes.statsItem}
            item
          >
            <AccessTimeIcon
              className={classes.statsIcon}
              color="action"
            />
            <Typography
              color="textSecondary"
              display="inline"
              variant="body2"
            >
              Updated 2hr ago
            </Typography>
          </Grid>
          <Grid
            className={classes.statsItem}
            item
          >
            <GetAppIcon
              className={classes.statsIcon}
              color="action"
            />
            <Typography
              color="textSecondary"
              display="inline"
              variant="body2"
            >
              {' '}
              Downloads
            </Typography>
          </Grid>
        </Grid>
      </Box>
    </Card>
  );
};

/*
ProductCard.propTypes = {
  className: PropTypes.string,
  product: PropTypes.object.isRequired
};
*/

export default ProductCard;
