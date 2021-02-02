from rest_framework import serializers, exceptions, views, generics, response, request, status
from rest_framework.decorators import action
from rest_framework import mixins, viewsets
from rest_framework import permissions, authentication
from django.core.cache import cache
from user.models import User
from server.settings import LOGIN_TIMEOUT, ROOT_USERS
import uuid
from server import permissions

class _UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__' # 所有字段
        # fields = '__all__': 表示所有字段
        # exclude = ('add_time',):  除去指定的某些字段
        # 这三种方式，存在一个即可

    #def validate(self, attrs):
    #    print('--- validate')
    #    print(attrs['u_is_admin'])
        # 对密码进行加密 make_password
        # attrs['u_passwd'] = make_password(attrs['u_passwd'])
    #    if attrs['u_uname'] in ADMIN_USERS:
    #        attrs['u_is_admin'] = True
     #   return attrs



class ListUsersView(generics.ListAPIView):
    serializer_class = _UsersSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsRootUser,)


class RetrieveUserView(generics.RetrieveAPIView):
    serializer_class = _UsersSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedAndSelf,)


class DeleteUserView(generics.DestroyAPIView):
    serializer_class = _UsersSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsRootUser,)


class _UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('u_uname','u_is_admin',) # 除去指定的某些字段


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = _UpdateUserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticatedAndSelf,)


class _ChangeAdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('u_id','u_is_admin')


class ChangeAmindUserView(generics.UpdateAPIView):
    serializer_class = _ChangeAdminUserSerializer
    queryset = User.objects.all()
    permission_classes = (permissions.IsRootUser,)


'''
class UsersView(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = User.objects.all()
    authentication_classes = (LoginTokenAuth,)
    permission_classes = (RootPermission,)

    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        print(action)
        if action == 'register': # 注册 path/?action=register
            return self.create(request, *args, **kwargs)
        if action == 'login':    # 登陆 path/?action=login
            return self._login(request)

    #@action(methods=['post'], detail=False)
    def _login(self, request):
        u_uname = request.data.get('u_uname')
        u_passwd = request.data.get('u_passwd')
        try:
            user = User.objects.get(u_uname=u_uname)
            if user.u_passwd != u_passwd:
                raise exceptions.AuthenticationFailed
            token = uuid.uuid4().hex
            cache.set(token, user.u_id, timeout=LOGIN_TIMEOUT) # 往缓存里添加数据
            data = {
                'msg': 'login success',
                'status': 200,
                'token': token}
            return response.Response(data)
        except User.DoesNotExist:
            raise exceptions.NotFound
        raise exceptions.ValidationError

    # 重写 get_serializer_class() 根据不同的action返回不同的序列化器
    def get_serializer_class(self):
        if self.action == 'post':
            return UserRegisterSerializer
        return UserSerializer

    # 重写create()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        # 创建管理员用户
        data = serializer.data
        if data["u_uname"] in ADMIN_USERS:
            u_id= data["u_id"]
            user = User.objects.get(pk=u_id)
            user.u_is_admin = True
            user.save()
            data["u_is_admin"] = True
        headers = self.get_success_headers(data)
        return response.Response(data, status=status.HTTP_201_CREATED, headers=headers)
'''

'''
class LoginTokenAuth(authentication.BaseAuthentication):
    # 用户成功登录后才能认证成功
    def authenticate(self, request):
        token = request.query_params.get('token')
        try:
            id = cache.get(token)
            user = User.objects.get(pk=id)
            return user, token # 认证成功返回一个元组(user, token)
        except:
            return None # 认证失败返回None

# root用户可以get所有的user, 其它用户只能GET自己的详情
class UsersPermission(permissions.BasePermission):
    def has_permission(self, request:request.Request, view):
        if request.method == 'GET':
            if isinstance(request.user, User):
                if request.user.u_uname in ROOT_USERS:
                    return True

        return True


# 只有root用户才能删除
class RootPermissionForDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if isinstance(request.user, User):
                if request.user.u_uname in ROOT_USERS:
                    return True
            return False
        return True

# 管理员用户才能list users
class RootPermissionForList(permissions.BasePermission):
    def has_permission(self, request:request.Request, view):
        if 'list' in request.path:
            if isinstance(request.user, User):
                return request.user.u_is_admin
            return False
        return True
'''
