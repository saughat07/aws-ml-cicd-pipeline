output "repository_url" {
  value = aws_codecommit_repository.ml_repo.clone_url_http
}
