package com.pic2cheese.service;

import com.pic2cheese.api.User;
import com.pic2cheese.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public Long join(User user) {

        User userEntity = new User();

        userEntity.setGender(user.getGender());
        userEntity.setName(user.getName());
        userEntity.setNickname(user.getNickname());
        userEntity.setAge(user.getAge());
        userEntity.setPw(user.getPw());
        userEntity.setCity(user.getCity());
        userEntity.setStreet(user.getStreet());
        userEntity.setZipcode(user.getZipcode());
        userEntity.setJoinDay(LocalDateTime.now());

        vaildateDuplicateUser(userEntity);
        userRepository.save(userEntity);

        return userEntity.getId();
    }

    public List<User> list() {
        return userRepository.findAll();
    }

    public User findOne(Long userId){
        return userRepository.findOne(userId);
    }

    public void modify(User user) throws Exception {
        User userEntity = userRepository.findOne(user.getId());

        userEntity.setZipcode(user.getZipcode());
        userEntity.setStreet(user.getStreet());
        userEntity.setCity(user.getCity());
        userEntity.setPw(user.getPw());

        userRepository.save(userEntity);
    }

    public void remove(Long userNo) throws Exception {
        userRepository.deleteById(userNo);
    }



    private void vaildateDuplicateUser(User user) {
        List<User> findUsers = userRepository.finById(user.getId());
        if (!findUsers.isEmpty()) {
            throw new IllegalStateException("이미 존재하는 회원");
        }
    }
}
